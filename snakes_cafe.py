from textwrap import dedent
import sys
import uuid

WIDTH = 96

menu = [
    {"item": "wings", "count": 0, "kind": "appetizers", "price": 5.00, "quantity": 10},
    {"item": "bacon bites", "count": 0, "kind": "appetizers", "price": 7.00, "quantity": 10},
    {"item": "pork buns", "count": 0, "kind": "appetizers", "price": 6.00, "quantity": 10},
    {"item": "brush with death", "count": 0, "kind": "appetizers", "price": 6.00, "quantity": 10},
    {"item": "cookies", "count": 0, "kind": "appetizers", "price": 5.00, "quantity": 10},
    {"item": "spring rolls", "count": 0, "kind": "appetizers", "price": 6.00, "quantity": 10},
    {"item": "pizza bagles", "count": 0, "kind": "appetizers", "price": 3.00, "quantity": 10},
    {"item": "cheese sticks", "count": 0, "kind": "appetizers", "price": 6.00, "quantity": 10},
    {"item": "gyoza", "count": 0, "kind": "appetizers", "price": 7.00, "quantity": 10},

    {"item": "salmon", "count": 0, "kind": "entrees", "price": 10, "quantity": 10},
    {"item": "steak", "count": 0, "kind": "entrees", "price": 15.00, "quantity": 10},
    {"item": "meat tornado", "count": 0, "kind": "entrees", "price": 25.00, "quantity": 10},
    {"item": "a literal garden", "count": 0, "kind": "entrees", "price": 26.00, "quantity": 10},
    {"item": "garden gnomes", "count": 0, "kind": "entrees", "price": 35.00, "quantity": 10},
    {"item": "pasta", "count": 0, "kind": "entrees", "price": 25.00, "quantity": 10},
    {"item": "lasagna", "count": 0, "kind": "entrees", "price": 27.00, "quantity": 10},
    {"item": "lame salad", "count": 0, "kind": "entrees", "price": 26.00, "quantity": 10},
    {"item": "sad vampire", "count": 0, "kind": "entrees", "price": 28.00, "quantity": 10},


    {"item": "ice cream", "count": 0, "kind": "desserts", "price": 5.00, "quantity": 10},
    {"item": "cake", "count": 0, "kind": "desserts", "price": 9.00, "quantity": 10},
    {"item": "pie", "count": 0, "kind": "desserts", "price": 8.00, "quantity": 10},
    {"item": "banana split", "count": 0, "kind": "desserts", "price": 11.00, "quantity": 10},
    {"item": "fairy dust", "count": 0, "kind": "desserts", "price": 111.00, "quantity": 10},
    {"item": "solid cocktail", "count": 0, "kind": "desserts", "price": 4.00, "quantity": 10},
    {"item": "cup of dirt", "count": 0, "kind": "desserts", "price": 7.00, "quantity": 10},
    {"item": "bread pudding", "count": 0, "kind": "desserts", "price": 9.00, "quantity": 10},
    {"item": "solitude", "count": 0, "kind": "desserts", "price": 3.00, "quantity": 10},


    {"item": "coffee", "count": 0, "kind": "drinks", "price": 45.00, "quantity": 10},
    {"item": "tea", "count": 0, "kind": "drinks", "price": 3.00, "quantity": 10},
    {"item": "blood of the innocent", "count": 0, "kind": "drinks", "price": 5.00, "quantity": 10},
    {"item": "cranberry juice", "count": 0, "kind": "drinks", "price": 7.00, "quantity": 10},
    {"item": "wine", "count": 0, "kind": "drinks", "price": 99.00, "quantity": 10},
    {"item": "milk", "count": 0, "kind": "drinks", "price": 88.00, "quantity": 10},
    {"item": "newt broth", "count": 0, "kind": "drinks", "price": 3.00, "quantity": 10},
    {"item": "water", "count": 0, "kind": "drinks", "price": 2.00, "quantity": 10},
    {"item": "pain", "count": 0, "kind": "drinks", "price": 11.00, "quantity": 10},



    {"item": "gummy worms", "count": 0, "kind": "sides", "price": 2.00, "quantity": 10},
    {"item": "mashed potatoes", "count": 0, "kind": "sides", "price": 2.00, "quantity": 10},
    {"item": "frog eyes", "count": 0, "kind": "sides", "price": 7.00, "quantity": 10},
    {"item": "ketchup", "count": 0, "kind": "sides", "price": 4.00, "quantity": 10},
    {"item": "fruit", "count": 0, "kind": "sides", "price": 12.00, "quantity": 10},
    {"item": "edible flowers", "count": 0, "kind": "sides", "price": 33.00, "quantity": 10},
    {"item": "meatballs", "count": 0, "kind": "sides", "price": 3.00, "quantity": 10},
    {"item": "rage", "count": 0, "kind": "sides", "price": 2.00, "quantity": 10},
    {"item": "joy", "count": 0, "kind": "sides", "price": 1.00, "quantity": 10},

]


order = []


def greeting():
    """Function that greets the user and shows the menu.
    """
    ln_one = 'Welcome to the Snakes Cafe!'
    ln_two = 'Please see our menu below.'
    ln_three = 'To quit at any time, type "quit"'
    ln_four = 'To view menu, type "menu"'
    print(dedent(f'''
            {'*' * WIDTH}
            {' ' * ((WIDTH - len(ln_one) // 2)) + ln_one + (' ' * ((WIDTH - len(ln_one)) // 2))}
            {' ' * ((WIDTH - len(ln_two) // 2)) + ln_two + (' ' * ((WIDTH - len(ln_two)) // 2))}

            {' ' * ((WIDTH - len(ln_three) // 2)) + ln_three + (' ' * ((WIDTH - len(ln_three)) // 2))}

             {' ' * ((WIDTH - len(ln_four) // 2)) + ln_four + (' ' * ((WIDTH - len(ln_four)) // 2))}

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
            print(str(i['item']) + ' $' + str(i['price']))

    print(' \n')
    print('Entrees')
    print('----------')
    for i in menu:
        if i['kind'] == 'entrees':
            print(str(i['item']) + ' $' + str(i['price']))

    print(' \n')
    print('Desserts')
    print('----------')
    for i in menu:
        if i['kind'] == 'desserts':
            print(str(i['item']) + ' $' + str(i['price']))

    print(' \n')
    print('Drinks')
    print('----------')
    for i in menu:
        if i['kind'] == 'drinks':
            print(str(i['item']) + ' $' + str(i['price']))
    print(' \n')

    print(' \n')
    print('Sides')
    print('----------')
    for i in menu:
        if i['kind'] == 'sides':
            print(str(i['item']) + ' $' + str(i['price']))
    print(' \n')


def remove(order_to_remove):
    """
    removes an item from the order
    """
    if order_to_remove in order:
        order.remove(order_to_remove)
        for i in menu:
            if i['count'] > 0:
                i['count'] = i['count'] - 1
        print('One order of ' + order_to_remove + ' removed')


def display_selected_category(selected_kind):
    """
    Shows the items in a category that the user types
    """
    for i in menu:
        if i['kind'] == selected_kind:
            print(i['item'])


def check():
    """
    checks the user input for exit, if item already in cart, or if user input is invalid
    """
    user_input = input('What would you like to order? Or type "order" to see what is in your cart: ').lower()
    if user_input == 'quit':
        exit()
    if user_input == 'menu':
        generate_menu()

    if user_input == 'order':
        display_order()

    if user_input.find('remove') != -1:
        remove(user_input[7:])

    for i in menu:
        if user_input == i['kind']:
            display_selected_category(user_input)

    for i in menu:
        if user_input == i['item']:
            if user_input in order:
                i['count'] += 1
                print('You must be hungry! Now you have ' + str(i['count']) + ' orders of ' + user_input + '!')
                order_total = 0
                for i in menu:
                    if i['item'] in order:
                        order_total += i['price']
                print('Subtotal $' + str(order_total))
                order.append(user_input)
            else:
                print('One order of ' + user_input + ' has been added to your cart! ')
                order_total = 0
                for i in menu:
                    if i['item'] == user_input:
                        order_total += i['price']
                print('Subtotal $' + str(order_total))
                i['count'] = 1
                order.append(user_input)
            check()
    else:
        print('Please look at our menu and choose something we have!')
        check()


def run():
    greeting()
    generate_menu()
    check()


def display_order():
    """
    displays just the items being ordered
    """
    print(' \n')
    if not len(order):
        print('Your cart is empty!')
    for i in menu:
        if i['count'] > 0:
            print(str(i['item']) + ' x' + str(i['count']) + ' $' + str(i['price']))


def total_cost():
    """
    totals the cost of the order
    """
    order_total = 0
    for i in menu:
        if i['item'] in order:
            order_total += i['price']
    tax = order_total * 0.101
    total_with_tax = tax + order_total
    print('--------------------------------')
    print('Subtotal $' + str(order_total))
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
    display_order()
    print('------------------------------')
    total_cost()
    sys.exit()


if __name__ == '__main__':
    """
    runs the file on start
    """
    run()

"""
dictionary of dictionaries
category item, price, quantity
"""
