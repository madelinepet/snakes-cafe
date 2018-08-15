from textwrap import dedent
import sys

WIDTH = 96

BANK = [
    {
        'question': 'What would you like to order?',
        'number': 0,
    },
]
menu = [
    {"item": "wings", "count": 0, "kind": "appetizers", "price": 5},
    {"item": "cookies", "count": 0, "kind": "appetizers", "price": 4},
    {"item": "spring rolls", "count": 0, "kind": "appetizers", "price": 6},
    {"item": "pizza bagles", "count": 0, "kind": "appetizers", "price": 3},
    {"item": "cheese sticks", "count": 0, "kind": "appetizers", "price": 6},
    {"item": "gyoza", "count": 0, "kind": "appetizers", "price": 7},
    {"item": "salmon", "count": 0, "kind": "entrees", "price": 10},
    {"item": "steak", "count": 0, "kind": "entrees", "price": 15},
    {"item": "meat tornado", "count": 0, "kind": "entrees", "price": 25},
    {"item": "a literal garden", "count": 0, "kind": "entrees", "price": 26},
    {"item": "garden gnomes", "count": 0, "kind": "entrees", "price": 35},
    {"item": "pasta", "count": 0, "kind": "entrees", "price": 25},
    {"item": "ice cream", "count": 0, "kind": "desserts", "price": 5},
    {"item": "cake", "count": 0, "kind": "desserts", "price": 5},
    {"item": "pie", "count": 0, "kind": "desserts", "price": 5},
    {"item": "banana split", "count": 0, "kind": "desserts", "price": 5},
    {"item": "fairy dust", "count": 0, "kind": "desserts", "price": 5},
    {"item": "solid cocktail", "count": 0, "kind": "desserts", "price": 5},
    {"item": "coffee", "count": 0, "kind": "drinks", "price": 5},
    {"item": "tea", "count": 0, "kind": "drinks", "price": 5},
    {"item": "blood of the innocent", "count": 0, "kind": "drinks", "price": 5},
    {"item": "cranberry juice", "count": 0, "kind": "drinks", "price": 5},
    {"item": "wine", "count": 0, "kind": "drinks", "price": 5},
    {"item": "milk", "count": 0, "kind": "drinks", "price": 5},
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
            print(i['item'])

    print(' \n')
    print('Entrees')
    print('----------')
    for i in menu:
        if i['kind'] == 'entrees':
            print(i['item'])

    print(' \n')
    print('Desserts')
    print('----------')
    for i in menu:
        if i['kind'] == 'desserts':
            print(i['item'])

    print(' \n')
    print('Drinks')
    print('----------')
    for i in menu:
        if i['kind'] == 'drinks':
            print(i['item'])
    print(' \n')


def check():
    """
    checks the user input for exit, if item already in cart, or if user input is invalid
    """
    user_input = input('What would you like to order? ').lower()
    if user_input == 'quit':
        exit()
    if user_input == 'menu':
        print('in if')
        generate_menu()

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


def exit():
    print(dedent('''
    Thank you! Your order has been placed!
    '''))
    sys.exit()


if __name__ == '__main__':
    run()
