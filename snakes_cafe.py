from textwrap import dedent
import sys
import uuid
import csv

WIDTH = 96

# import pdb; pdb.set_trace()
try:
    with open('menu.csv', newline='') as csvfile:
            lines = csv.DictReader(csvfile)
            menu = []
            for row in lines:
                dict_row = dict(row)
                dict_row['price'] = float(dict_row['price'])
                dict_row['quantity'] = int(dict_row['quantity'])
                dict_row['count'] = 0
                menu.append(dict_row)
except:

    menu = [
        {"item": "wings", "count": 0, "kind": "appetizers", "price": 5.11, "quantity": 10},
        {"item": "bacon bites", "count": 0, "kind": "appetizers", "price": 7.11, "quantity": 10},
        {"item": "pork buns", "count": 0, "kind": "appetizers", "price": 6.11, "quantity": 10},
        {"item": "brush with death", "count": 0, "kind": "appetizers", "price": 6.11, "quantity": 10},
        {"item": "cookies", "count": 0, "kind": "appetizers", "price": 5.11, "quantity": 10},
        {"item": "spring rolls", "count": 0, "kind": "appetizers", "price": 6.11, "quantity": 10},
        {"item": "pizza bagles", "count": 0, "kind": "appetizers", "price": 3.11, "quantity": 10},
        {"item": "cheese sticks", "count": 0, "kind": "appetizers", "price": 6.11, "quantity": 10},
        {"item": "gyoza", "count": 0, "kind": "appetizers", "price": 7.11, "quantity": 10},

        {"item": "salmon", "count": 0, "kind": "entrees", "price": 10.99, "quantity": 10},
        {"item": "steak", "count": 0, "kind": "entrees", "price": 15.99, "quantity": 10},
        {"item": "meat tornado", "count": 0, "kind": "entrees", "price": 25.99, "quantity": 10},
        {"item": "a literal garden", "count": 0, "kind": "entrees", "price": 26.99, "quantity": 10},
        {"item": "garden gnomes", "count": 0, "kind": "entrees", "price": 35.99, "quantity": 10},
        {"item": "pasta", "count": 0, "kind": "entrees", "price": 25.99, "quantity": 10},
        {"item": "lasagna", "count": 0, "kind": "entrees", "price": 27.99, "quantity": 10},
        {"item": "lame salad", "count": 0, "kind": "entrees", "price": 26.99, "quantity": 10},
        {"item": "sad vampire", "count": 0, "kind": "entrees", "price": 28.99, "quantity": 10},


        {"item": "ice cream", "count": 0, "kind": "desserts", "price": 5.22, "quantity": 10},
        {"item": "cake", "count": 0, "kind": "desserts", "price": 9.22, "quantity": 10},
        {"item": "pie", "count": 0, "kind": "desserts", "price": 8.22, "quantity": 10},
        {"item": "banana split", "count": 0, "kind": "desserts", "price": 11.22, "quantity": 10},
        {"item": "fairy dust", "count": 0, "kind": "desserts", "price": 111.22, "quantity": 10},
        {"item": "solid cocktail", "count": 0, "kind": "desserts", "price": 4.22, "quantity": 10},
        {"item": "cup of dirt", "count": 0, "kind": "desserts", "price": 7.22, "quantity": 10},
        {"item": "bread pudding", "count": 0, "kind": "desserts", "price": 9.22, "quantity": 10},
        {"item": "solitude", "count": 0, "kind": "desserts", "price": 3.22, "quantity": 10},


        {"item": "coffee", "count": 0, "kind": "drinks", "price": 45.33, "quantity": 10},
        {"item": "tea", "count": 0, "kind": "drinks", "price": 3.33, "quantity": 10},
        {"item": "blood of the innocent", "count": 0, "kind": "drinks", "price": 5.33, "quantity": 10},
        {"item": "cranberry juice", "count": 0, "kind": "drinks", "price": 7.33, "quantity": 10},
        {"item": "wine", "count": 0, "kind": "drinks", "price": 99.33, "quantity": 10},
        {"item": "milk", "count": 0, "kind": "drinks", "price": 88.33, "quantity": 10},
        {"item": "newt broth", "count": 0, "kind": "drinks", "price": 3.33, "quantity": 10},
        {"item": "water", "count": 0, "kind": "drinks", "price": 2.33, "quantity": 10},
        {"item": "pain", "count": 0, "kind": "drinks", "price": 11.33, "quantity": 10},



        {"item": "gummy worms", "count": 0, "kind": "sides", "price": 2.44, "quantity": 10},
        {"item": "mashed potatoes", "count": 0, "kind": "sides", "price": 2.44, "quantity": 10},
        {"item": "frog eyes", "count": 0, "kind": "sides", "price": 7.44, "quantity": 10},
        {"item": "ketchup", "count": 0, "kind": "sides", "price": 4.44, "quantity": 10},
        {"item": "fruit", "count": 0, "kind": "sides", "price": 12.44, "quantity": 10},
        {"item": "edible flowers", "count": 0, "kind": "sides", "price": 33.44, "quantity": 10},
        {"item": "meatballs", "count": 0, "kind": "sides", "price": 3.44, "quantity": 10},
        {"item": "rage", "count": 0, "kind": "sides", "price": 2.44, "quantity": 10},
        {"item": "joy", "count": 0, "kind": "sides", "price": 1.44, "quantity": 10},

    ]
order_list = []
order_total_before_tax = 0


class Order:

    def __init__(self, uuid, order_list, count=None):
        """ Constructs the initial instace
        """
        self.uuid = uuid
        self.order_list = order_list
        self.count = count

    def add_item(self, user_input):
        """ Adds items to cart
        """
        global order_total_before_tax
        for i in menu:
            if user_input == i['item']:
                    if user_input in order_list:
                            i['count'] += 1
                            print('You must be hungry! Now you have ' + str(i['count']) + ' orders of ' + user_input + '!')
                            for i in menu:
                                if i['item'] in order_list:
                                    order_total_before_tax += i['price']
                            print('Subtotal $' + str(round(order_total_before_tax, 2)))
                            order_list.append(user_input)
                    else:
                        print('One order of ' + user_input + ' has been added to your cart! ')
        for i in menu:
            if i['item'] == user_input:
                order_total_before_tax += i['price']
                print('Subtotal $' + str(round(order_total_before_tax, 2)))
                i['count'] = 1
                order_list.append(user_input)
        # check()

    def remove_item(self, user_input, count=1):
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

    def display_order(self, order_list):
        """ Display the order and total to the screen
        """
        print(' \n')
        if not len(order_list):
            print('Your cart is empty!')
        for i in menu:
            if i['count'] > 0:
                print(str(i['item']) + ' x' + str(i['count']) + ' $' + str(round(i['price'], 2)))

    def print_receipt(self, order_list, count):
        """ Prints the receipt to another file
        """
        pass

    def __repr__(self):
        """ Formatting for anything that needs to be read by humans
        """
        pass


specific_order = Order(uuid, order_list)


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


def generate_menu():
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


def check():
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
        Order.display_order(specific_order, order_list)

    elif user_input.find('remove') != -1:
        Order.remove_item(user_input[7:])

    for i in menu:
        if user_input == i['kind']:
            print(i['item'] + str(i['price']))
    for i in menu:
        if input_list[0] == i['item']:
            specific_order.add_item(user_input)
            if (len(input_list) > 1):
                i['count'] = input_list[1]
            else:
                i['count'] = 1
        else:
            pass


def run():
    greeting()
    generate_menu()
    check()


def total_cost():
    """
    totals the cost of the order
    """
    global order_total_before_tax
    for i in menu:
        if i['item'] in order_list:
            order_total_before_tax += i['price']
    tax = order_total_before_tax * 0.101
    total_with_tax = tax + order_total_before_tax
    print('--------------------------------')
    print('Subtotal $' + str(round(order_total_before_tax, 2)))
    print(' \n')
    print('Sales Tax $' + str(round(tax, 2)))
    print(' \n')
    print('Total Due $' + str(round(total_with_tax, 2)))
    print('**********************************')


def exit():
    """
    displays receipt and exits
    """
    order_num = uuid.uuid4()
    print('The Snakes Cafe')
    print('Eatability Counts')

    print('Order #' + str(order_num))
    print('==============================')
    print('------------------------------')
    total_cost()
    sys.exit()


if __name__ == '__main__':
    """
    runs the file on start
    """
try:
    run()
except KeyboardInterrupt:
    exit()
