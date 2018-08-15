from textwrap import dedent
import sys
import uuid

WIDTH = 96

menu = [
    {"item": "wings", "count": 0, "kind": "appetizers", "price": 5.00},
    {"item": "bacon bites", "count": 0, "kind": "appetizers", "price": 7.00},
    {"item": "pork buns", "count": 0, "kind": "appetizers", "price": 6.00},
    {"item": "brush with death", "count": 0, "kind": "appetizers", "price": 6.00},
    {"item": "cookies", "count": 0, "kind": "appetizers", "price": 5.00},
    {"item": "spring rolls", "count": 0, "kind": "appetizers", "price": 6.00},
    {"item": "pizza bagles", "count": 0, "kind": "appetizers", "price": 3.00},
    {"item": "cheese sticks", "count": 0, "kind": "appetizers", "price": 6.00},
    {"item": "gyoza", "count": 0, "kind": "appetizers", "price": 7.00},

    {"item": "salmon", "count": 0, "kind": "entrees", "price": 10},
    {"item": "steak", "count": 0, "kind": "entrees", "price": 15.00},
    {"item": "meat tornado", "count": 0, "kind": "entrees", "price": 25.00},
    {"item": "a literal garden", "count": 0, "kind": "entrees", "price": 26.00},
    {"item": "garden gnomes", "count": 0, "kind": "entrees", "price": 35.00},
    {"item": "pasta", "count": 0, "kind": "entrees", "price": 25.00},
    {"item": "lasagna", "count": 0, "kind": "entrees", "price": 27.00},
    {"item": "lame salad", "count": 0, "kind": "entrees", "price": 26.00},
    {"item": "sad vampire", "count": 0, "kind": "entrees", "price": 28.00},


    {"item": "ice cream", "count": 0, "kind": "desserts", "price": 5.00},
    {"item": "cake", "count": 0, "kind": "desserts", "price": 9.00},
    {"item": "pie", "count": 0, "kind": "desserts", "price": 8.00},
    {"item": "banana split", "count": 0, "kind": "desserts", "price": 11.00},
    {"item": "fairy dust", "count": 0, "kind": "desserts", "price": 111.00},
    {"item": "solid cocktail", "count": 0, "kind": "desserts", "price": 4.00},
    {"item": "cup of dirt", "count": 0, "kind": "desserts", "price": 7.00},
    {"item": "bread pudding", "count": 0, "kind": "desserts", "price": 9.00},
    {"item": "solitude", "count": 0, "kind": "desserts", "price": 3.00},


    {"item": "coffee", "count": 0, "kind": "drinks", "price": 45.00},
    {"item": "tea", "count": 0, "kind": "drinks", "price": 3.00},
    {"item": "blood of the innocent", "count": 0, "kind": "drinks", "price": 5.00},
    {"item": "cranberry juice", "count": 0, "kind": "drinks", "price": 7.00},
    {"item": "wine", "count": 0, "kind": "drinks", "price": 99.00},
    {"item": "milk", "count": 0, "kind": "drinks", "price": 88.00},
    {"item": "newt broth", "count": 0, "kind": "drinks", "price": 3.00},
    {"item": "water", "count": 0, "kind": "drinks", "price": 2.00},
    {"item": "pain", "count": 0, "kind": "drinks", "price": 11.00},



    {"item": "gummy worms", "count": 0, "kind": "sides", "price": 2.00},
    {"item": "mashed potatoes", "count": 0, "kind": "sides", "price": 2.00},
    {"item": "frog eyes", "count": 0, "kind": "sides", "price": 7.00},
    {"item": "ketchup", "count": 0, "kind": "sides", "price": 4.00},
    {"item": "fruit", "count": 0, "kind": "sides", "price": 12.00},
    {"item": "edible flowers", "count": 0, "kind": "sides", "price": 33.00},
    {"item": "meatballs", "count": 0, "kind": "sides", "price": 3.00},
    {"item": "rage", "count": 0, "kind": "sides", "price": 2.00},
    {"item": "joy", "count": 0, "kind": "sides", "price": 1.00},

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
        if user_input == i['item']:
            if user_input in order:
                i['count'] += 1
                print('You must be hungry! Now you have ' + str(i['count']) + ' orders of ' + user_input  + '!')
                order.append(user_input)
            else:
                print('One order of ' + user_input + ' has been added to your cart! ')
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
    run()
