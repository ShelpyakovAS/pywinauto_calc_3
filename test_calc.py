"""
Модуль с тестами для class Calc
"""
import time
import pytest
from decorators import time_counter
import random


def calc_param(param_dict: dict):
    f"""
    Функция перобразует словарь в списки данных для автотестов.
    :param param_dict: - key(математичекое действие):[ random_num, ... , answer, 'assert Error']
    :return: param -> list [ str 'actions'(1+1+1+1=), num 4, str ''assert Error'']
    """
    param = []
    for key in param_dict:
        my_str = f'{param_dict[key][0]}'
        for i in range(len(key)):
            my_str += f'{key[i]}{param_dict[key][i+1]}'
        param.append([my_str+'=', param_dict[key][-2], param_dict[key][-1]])
    return param


random_num = [random.randint(1, 100) for i in range(8)]
my_dict = {
    '+': [random_num[0], random_num[1], random_num[0] + random_num[1], 'Addition error'],
    '-': [random_num[2], random_num[3], random_num[2] - random_num[3], 'Subtraction error'],
    '*': [random_num[4], random_num[5], random_num[4] * random_num[5], 'Multiplication error'],
    '/': [random_num[6], random_num[7], random_num[6] / random_num[7], 'Division error'],
    '+-*/': [random_num[0], random_num[1], random_num[2], random_num[3], random_num[4],
             (random_num[0] + random_num[1] - random_num[2]) * random_num[3] / random_num[4],
             'Calculation error'],
    '****': [random_num[0], random_num[1], random_num[2], random_num[3], random_num[4],
             random_num[0] * random_num[1] * random_num[2] * random_num[3] * random_num[4],
             'Calculation error'],
}


@time_counter
def test_calc_addition(app):
    """
    Проверка сложения программы Калькулятор (calc.exe)
    :param app: обьект class Calc
    :return: assert : 'Addition error'
    """
    app.actions('4+4=')
    assert app.get_answer() == '8', 'Addition error'


@time_counter
def test_calc_subtraction(app):
    """
    Проверка вычетания программы Калькулятор (calc.exe)
    :param app: обьект class Calc
    :return: assert : 'Subtraction error'
    """
    app.actions('56-15=')
    assert app.get_answer() == '41', 'Subtraction error'


@time_counter
def test_calc_multiply(app):
    """
    Проверка умножения программы Калькулятор (calc.exe)
    :param app: обьект class Calc
    :return: assert : 'Multiplication error'
    """
    app.actions('22*3=')
    assert app.get_answer() == '66', 'Multiplication error'


@time_counter
def test_calc_divide(app):
    """
    Проверка деления программы Калькулятор (calc.exe)
    :param app: обьект class Calc
    :return: assert : 'Division error'
    """
    app.actions('99/33=')
    assert app.get_answer() == '3', 'Division error'


@pytest.mark.parametrize('date', calc_param(my_dict))
def test_calc(app, date: list):
    """
    Проверка сложения, вычитания, умножения или деления Калькулятора (calc.exe)
    :param app: обьект class Calc
    :param date: list - [ str - действий для проверки('1+1='), num - результат действий(2), str - assert ]
    :return:
        assert : 'Addition error', 'Subtraction error', 'Multiplication error', 'Division error'.
    """
    app.actions(date[0])
    answer = app.dlg.child_window(auto_id="158", control_type="Text").window_text()
    if ',' in answer:
        assert round(float(answer.replace(',', '.')), 2) == round(date[1], 2), date[2]
    else:
        assert int(answer) == date[1], date[2]


# dlg.print_control_identifiers()