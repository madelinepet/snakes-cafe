from textwrap import dedent
import sys
import uuid
import csv

WIDTH = 96

# menu = []


def run():
    """ Runs the script, and error handles if path is bad
    """
    # global menu
    print('Which menu would you like to use? Your own .csv or our original menu?')
    menu_input = input('Type "original" or "csv": ')
    if menu_input == 'quit':
        exit()
    if menu_input == 'csv':
        file_path = input('What is your file path?: ')
        menu = load_csv(file_path)
        if menu == 'Invalid File':
            print('Please try again!')
            run()
        if menu == 'File Not Found':
            print('File not found, please try again or use our original menu.')
            run()

    else:
        menu = load_csv()

    greeting()
    generate_menu(menu)
    check(menu)


def load_csv(file_path='menu.csv'):
    """ Takes in file path and loads a menu based on it, original menu is also loaded frm csv
    """
    file_readable_to_file_path = file_path.split('/')
    file = file_readable_to_file_path[-1].split('.')
    extension = file[-1]
    if extension != 'csv':
        return 'Invalid File'
    else:
        try:
            with open(file_path, newline='') as csvfile:
                lines = csv.DictReader(csvfile)
                menu = []
                for row in lines:
                    dict_row = dict(row)
                    dict_row['price'] = float(dict_row['price'])
                    dict_row['quantity'] = int(dict_row['quantity'])
                    dict_row['count'] = 0
                    menu.append(dict_row)
                return menu
        except FileNotFoundError:
            return 'File Not Found'


order_total_before_tax = 0


class Order:

    def __init__(self, uuid, count=None):
        """ Constructs the initial instace
        """
        self.uuid = uuid
        self.order_dict = {}
        self.count = count

    def add_item(self, item, amount=1):
        """ Adds items to cart
        """
        global order_total_before_tax
        if item['item'] in self.order_dict:
            if self.order_dict[item['item']]['count'] + amount > item['quantity']:
                return 'We only have ' + str(item['quantity'] - self.order_dict[item['item']]['count']) + ' in stock! Please order fewer.'
            else:
                self.order_dict[item['item']]['count'] += amount
                order_total_before_tax += item['price'] * amount
                return 'You must be hungry! Now you have ' + str(self.order_dict[item['item']]['count']) + ' orders of ' + item['item'] + '!\n Subtotal $' + str(round(order_total_before_tax, 2))
        else:
            if amount > item['quantity']:
                return 'We only have ' + str(item['quantity']) + ' in stock! Please order fewer.'
            else:
                order_total_before_tax += item['price'] * amount
                self.order_dict[item['item']] = {'count': amount, 'price': item['price']}
                return str(amount) + ' order(s) of ' + item['item'] + ' has been added to your cart!\n Subtotal $' + str(round(order_total_before_tax, 2))

    def remove_item(self, user_input, menu, count=1):
        """
        removes an item from the order
        """
        if user_input in order_list:
            order_to_remove = user_input
            order_list.remove(order_to_remove)
            for i in menu:
                if i['count'] > 0:
                    i['count'] = i['count'] - 1
            print('One order of ' + order_to_remove + ' removed')
        check(menu)

    def display_order(self):
        """ Display the order and total to the screen
        """
        total = 0
        final_string_you_should_rename_this = ''
        if not len(specific_order.order_dict):
            return 'Your cart is empty!'
        for key in specific_order.order_dict.keys():
            item_total = round(specific_order.order_dict[key]['price'] * specific_order.order_dict[key]['count'], 2)
            # print(key + ' x' + str(specific_order.order_dict[key]['count']) + ' $' + str(item_total))
            final_string_you_should_rename_this = final_string_you_should_rename_this + key + ' x' + str(specific_order.order_dict[key]['count']) + ' $' + str(item_total) + '\n\n'
            total += item_total
        final_string_you_should_rename_this = final_string_you_should_rename_this + 'Your total before tax is $' + str(total)
        return final_string_you_should_rename_this

    def print_receipt(self):
        """ Prints the receipt to another file
        """
        with open(str(self.uuid) + '.txt', 'w') as f:
            f.write(self.display_order())

    def __repr__(self):
        """ Formatting for anything that needs to be read by humans
        """
        pass


specific_order = Order(uuid.uuid4())


def greeting():
    """Function that greets the user and shows the menu.
    """
    ln_one = 'Welcome to the Snakes Cafe!'
    ln_two = 'Please see our menu below.'
    ln_three = 'To quit at any time, type "quit"'
    ln_four = 'To view menu, type "menu"'
    ln_five = 'To view order, type "order"'
    print(dedent(f'''
            {'*' * WIDTH}
            {' ' * ((WIDTH - len(ln_one) // 2)) + ln_one + (' ' * ((WIDTH - len(ln_one)) // 2))}
            {' ' * ((WIDTH - len(ln_two) // 2)) + ln_two + (' ' * ((WIDTH - len(ln_two)) // 2))}

            {' ' * ((WIDTH - len(ln_three) // 2)) + ln_three + (' ' * ((WIDTH - len(ln_three)) // 2))}

            {' ' * ((WIDTH - len(ln_four) // 2)) + ln_four + (' ' * ((WIDTH - len(ln_four)) // 2))}
            {' ' * ((WIDTH - len(ln_five) // 2)) + ln_five + (' ' * ((WIDTH - len(ln_five)) // 2))}
            {'*' * WIDTH}
        '''))


def generate_menu(menu):
    """
    prints the full menu
    """
    print('Appetizers')
    print('-----------')
    for i in menu:
        if i['kind'] == 'appetizers':
            print(str(i['item']) + ' $' + str(round(i['price'], 2)))

    print(' \n')
    print('Entrees')
    print('----------')
    for i in menu:
        if i['kind'] == 'entrees':
            print(str(i['item']) + ' $' + str(round(i['price'], 2)))

    print(' \n')
    print('Desserts')
    print('----------')
    for i in menu:
        if i['kind'] == 'desserts':
            print(str(i['item']) + ' $' + str(round(i['price'], 2)))

    print(' \n')
    print('Drinks')
    print('----------')
    for i in menu:
        if i['kind'] == 'drinks':
            print(str(i['item']) + ' $' + str(round(i['price'], 2)))
    print(' \n')

    print(' \n')
    print('Sides')
    print('----------')
    for i in menu:
        if i['kind'] == 'sides':
            print(str(i['item']) + ' $' + str(round(i['price'], 2)))
    print(' \n')


def check(menu):
    """
    checks the user input for exit, if item already in cart, or if user input is invalid
    """
    global order_total_before_tax
    user_input = input('What would you like to order? Or type "order" to see what is in your cart: ').lower()
    input_list = user_input.split(' ')
    if user_input == 'quit':
        exit()
    elif user_input == 'menu':
        generate_menu()

    elif user_input == 'order':
        print(specific_order.display_order())

    elif user_input.find('remove') != -1:
        Order.remove_item(specific_order, user_input[7:])
    for i in menu:
        if user_input == i['kind']:
            print(i['item'] + str(i['price']))
        elif input_list[0] == i['item']:
            if (len(input_list) > 1):
                result = specific_order.add_item(i, int(input_list[-1]))
                print(result)
            else:
                result = specific_order.add_item(i)
                print(result)
        else:
            pass
    check(menu)


# def total_cost(menu):
#     """
#     totals the cost of the order
#     """
#     global order_total_before_tax
#     for i in menu:
#         if i['item'] in order_list:
#             order_total_before_tax += i['price']
#     tax = order_total_before_tax * 0.101
#     total_with_tax = tax + order_total_before_tax
#     print('--------------------------------')
#     print('Subtotal $' + str(round(order_total_before_tax, 2)))
#     print(' \n')
#     print('Sales Tax $' + str(round(tax, 2)))
#     print(' \n')
#     print('Total Due $' + str(round(total_with_tax, 2)))
#     print('**********************************')


def exit():
    """
    displays receipt and exits
    """
    # order_num = uuid.uuid4()
    print('The Snakes Cafe')
    print('Eatability Counts')
    print(specific_order.display_order())
    print('Order #' + str(specific_order.uuid))
    print('==============================')
    print('------------------------------')
    specific_order.print_receipt()
    # total_cost()
    sys.exit()


if __name__ == '__main__':
    """
    runs the file on start
    """
    try:
        run()
    except KeyboardInterrupt:
        exit()

