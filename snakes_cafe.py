from textwrap import dedent
import sys

WIDTH = 96

BANK = [
    {
        'question': 'What would you like to order?',
        'number': 0,
    },
]
appetizers = ['wings', 'cookies', 'spring rolls']

entrees = ['salmon', 'steak', 'meat tornado', 'a literal garden']

desserts = ['ice cream', 'cake', 'pie']

drinks = ['coffee', 'tea', 'blood of the innocent']

order = []

def greeting():
    """Function that greets the user and shows the menu.
    """
    ln_one = 'Welcome to the Snakes Cafe!'
    ln_two = 'Please see our menu below.'
    ln_three = 'To quit at any time, type "quit"'
    print(dedent(f'''
            {'*' * WIDTH}
            {' ' * ((WIDTH - len(ln_one) // 2)) + ln_one + (' ' * ((WIDTH - len(ln_one)) // 2))}
            {' ' * ((WIDTH - len(ln_two) // 2)) + ln_two + (' ' * ((WIDTH - len(ln_two)) // 2))}

            {' ' * ((WIDTH - len(ln_three) // 2)) + ln_three + (' ' * ((WIDTH - len(ln_three)) // 2))}
            {'*' * WIDTH}
        '''))
    print('Appetizers')
    print('-----------')
    for i in appetizers:
        print(i)

    print(' \n')
    print('Entrees')
    print('----------')
    for i in entrees:
        print(i)

    print(' \n')
    print('Desserts')
    print('----------')
    for i in desserts:
        print(i)

    print(' \n')
    print('Drinks')
    print('----------')
    for i in drinks:
        print(i)
    print(' \n')


def check():
    user_input = input('What would you like to order? ').lower()
    if user_input == 'quit':
        exit()
    elif user_input in appetizers or user_input in entrees or user_input in desserts or user_input in drinks:
        if user_input in order:
            print('You must be hungry! Now you have multiple orders of ' + user_input  + '!')
            order.append(user_input)
        else:
            print('One order of ' + user_input + ' has been added to your cart! ')
            order.append(user_input)
        check()
    else:
        print('Please look at our menu and choose something we have!')
        check()

def run():
    greeting()
    check()

def exit():
    print(dedent('''
    Thank you! Your order has been placed!
    '''))
    sys.exit()

if __name__ == '__main__':
    run()
