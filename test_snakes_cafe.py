import snakes_cafe as sc

import pytest


def test_return_csv_returns_false_if_invalid_fp():
    """ Tests that when a invalid file path is given, returns 'Invalid File'
    """
    assert sc.load_csv('This is not a good file path') == 'Invalid File'

""" Test all endpoints of add_item (every rtn)
"""


def test_if_item_user_input_already_in_dict_but_qty_exceeded():
    """ Tests that program rtns message that qty has been exceeded if input twice
    """
    sc.add_item('Milk', 9)
    sc.add_item('Milk', 9) == 'We only have ' + str(item['quantity'] - self.order_dict[item['item']]['count']) + ' in stock! Please order fewer.'


def test_if_item_not_in_order_dict_qty_exceeded():
    """ Tests that program rtns message that qty has been exceeded if input once
    """
    assert sc.add_item('Milk', 11) == 'We only have ' + str(item['quantity'] - self.order_dict[item['item']]['count']) + ' in stock! Please order fewer.'


def test_item_adds_already_in_order_dict():
    sc.add_item('Milk', 1)
    assert sc.add_item('Milk', 8) == 'You must be hungry! Now you have ' + str(self.order_dict[item['item']]['count']) + ' orders of ' + item['item'] + '!\n Subtotal $' + str(round(order_total_before_tax, 2))


def test_item_adds_not_in_order_dict():
    assert  str(amount) + ' order(s) of ' + item['item'] + ' has been added to your cart!\n Subtotal $' + str(round(order_total_before_tax, 2))

def test_remove_item_removes_cost_of_item():
    sc.add_item('Milk', 1)
    sc.remove_item('Milk')
    assert self.order_dict[item['item']]['count'] == 0





