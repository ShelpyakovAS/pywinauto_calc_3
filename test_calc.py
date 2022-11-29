import time
import pytest
from decorators import time_counter
import random

random_num = [random.randint(1, 100) for i in range(8)]
my_dict = {
    '+': [random_num[0], random_num[1], random_num[0] + random_num[1], 'Addition error'],
    '-': [random_num[2], random_num[3], random_num[2] - random_num[3], 'Subtraction error'],
    '*': [random_num[4], random_num[5], random_num[4] * random_num[5], 'Multiplication error'],
    '/': [random_num[6], random_num[7], random_num[6] / random_num[7], 'Division error'],
}


@time_counter
def test_calc_addition(app):
    app.actions('4+4=')
    assert app.get_answer() == '8', 'Addition error'


@time_counter
def test_calc_subtraction(app):
    app.actions('56-15=')
    assert app.get_answer() == '41', 'Subtraction error'


@time_counter
def test_calc_multiply(app):
    app.actions('22*3=')
    assert app.get_answer() == '66', 'Multiplication error'


@time_counter
def test_calc_divide(app):
    app.actions('99/33=')
    assert app.get_answer() == '3', 'Division error'


@pytest.mark.parametrize('date', [[f'{my_dict[key][0]}{key}{my_dict[key][1]}=', my_dict[key][2], key] for key in my_dict])
def test_calc(app, date: list):
    app.actions(date[0])
    answer = app.dlg.child_window(auto_id="158", control_type="Text").window_text()
    if ',' in answer:
        assert float(answer.replace(',', '.')) == date[1], date[2]
    else:
        assert int(answer) == date[1], date[2]


# dlg.print_control_identifiers()