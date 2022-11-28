import time
import pytest
from decorators import time_counter


@time_counter
def test_calc_addition(dlg):
    '''dlg.print_control_identifiers()
    dlg.child_window(title="1").click()
    dlg.child_window(title="Сложение").click()
    dlg.child_window(title="1").click()
    dlg.child_window(auto_id="121", control_type="Button").click()'''
    dlg.type_keys('1+1=')
    answer = dlg.child_window(auto_id="158", control_type="Text")
    assert answer.window_text() == '2', 'Addition error'


@time_counter
def test_calc_subtraction(dlg):
    dlg.type_keys('3-1=')
    answer = dlg.child_window(auto_id="158", control_type="Text")
    dlg.print_control_identifiers()
    print(answer.window_text())
    assert answer.window_text() == '2', 'Subtraction error'


@time_counter
def test_calc_multiply(dlg):
    dlg.type_keys('4*3=')
    answer = dlg.child_window(auto_id="158", control_type="Text")
    assert answer.window_text() == '12', 'Multiply error'


@time_counter
def test_calc_divide(dlg):
    dlg.type_keys('9/3=')
    answer = dlg.child_window(auto_id="158", control_type="Text")
    assert answer.window_text() == '3', 'Divide error'


# dlg.print_control_identifiers()