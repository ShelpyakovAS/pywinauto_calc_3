"""
Модуль с декораторами
"""


import time


def time_counter(function):
    """
    Фукция для посчета времни выполнения автотеста и вывода результата в консоль.
    :arg:
        function: функция
    :return:
        None
    """

    def wrapper(app):
        start_time = time.time()
        function(app)
        print(start_time - time.time())

    return wrapper