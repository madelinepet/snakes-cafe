from textwrap import dedent
import sys
import uuid
import csv

WIDTH = 96

original_menu = [
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
    menu = original_menu

order = []
order_total_before_tax = 0


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


def add_to_cart(user_input):
    """
    Manages the adding of items to cart
    """
    global order_total_before_tax
    for i in menu:
        if user_input == i['item']:
                if user_input in order:
                        i['count'] += 1
                        print('You must be hungry! Now you have ' + str(i['count']) + ' orders of ' + user_input + '!')
                        for i in menu:
                            if i['item'] in order:
                                order_total_before_tax += i['price']
                        print('Subtotal $' + str(round(order_total_before_tax, 2)))
                        order.append(user_input)
                else:
                    print('One order of ' + user_input + ' has been added to your cart! ')
    for i in menu:
        if i['item'] == user_input:
            order_total_before_tax += i['price']
            print('Subtotal $' + str(round(order_total_before_tax, 2)))
            i['count'] = 1
            order.append(user_input)
    check()


def check():
    """
    checks the user input for exit, if item already in cart, or if user input is invalid
    """
    global order_total_before_tax
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
            print(i['item'] + str(i['price']))

    for i in menu:
        if user_input == i['item']:
            add_to_cart(user_input)
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
            print(str(i['item']) + ' x' + str(i['count']) + ' $' + str(round(i['price'], 2)))


def total_cost():
    """
    totals the cost of the order
    """
    global order_total_before_tax
    for i in menu:
        if i['item'] in order:
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
