import snakes_cafe as sc

import pytest


# def test_remove_module_exists():
#     assert sc.remove_item


# def test_check_module_exists():
#     assert sc.check


# def test_run_module_exists():
#     assert sc.run


# def test_display_order_module_exists():
#     assert sc.display_order


# def test_total_cost_module_exists():
#     assert sc.total_cost


def test_return_csv_returnss_false_if_invalid_fp():
    assert sc.load_csv('This is not a good file path') == 'Invalid File'

""" Test all endpoints of add_item (every rtn)
"""

# def test_add_to_cart():
#     add_to_cart('wings')
#     assert order_total_before_tax == 5.11

