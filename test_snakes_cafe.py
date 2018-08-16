from snakes_cafe import remove
from snakes_cafe import check
from snakes_cafe import run
from snakes_cafe import display_order
from snakes_cafe import total_cost
from snakes_cafe import add_to_cart
from snakes_cafe import order_total_before_tax


import pytest


def test_remove_module_exists():
    assert remove


def test_check_module_exists():
    assert check


def test_run_module_exists():
    assert run


def test_display_order_module_exists():
    assert display_order


def test_total_cost_module_exists():
    assert total_cost


# def test_add_to_cart():
#     add_to_cart('wings')
#     assert order_total_before_tax == 5.11

