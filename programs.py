"""
Модуль с классами управления порграммами
"""
from pywinauto import Desktop, Application
import random


class Calc:
    """
    Класс методов для работы с калькулятором (calc.exe).
    Args:
        None
    Attributes:
        app: запуск calc.exe
        dlg: подключение к окну Калькулятор
        calc_buttons: словарь доступа к кнопкам калькулятора
    """
    def __init__(self):
        self.app = Application(backend="uia").start('calc.exe')
        self.dlg = Desktop(backend="uia").Калькулятор
        self.calc_buttons = {
            '0': self.dlg.child_window(title="0", control_type="Button"),
            '1': self.dlg.child_window(title="1", control_type="Button"),
            '2': self.dlg.child_window(title="2", control_type="Button"),
            '3': self.dlg.child_window(title="3", control_type="Button"),
            '4': self.dlg.child_window(title="4", control_type="Button"),
            '5': self.dlg.child_window(title="5", control_type="Button"),
            '6': self.dlg.child_window(title="6", control_type="Button"),
            '7': self.dlg.child_window(title="7", control_type="Button"),
            '8': self.dlg.child_window(title="8", control_type="Button"),
            '9': self.dlg.child_window(title="9", control_type="Button"),
            '+': self.dlg.child_window(title="Сложение", control_type="Button"),
            '-': self.dlg.child_window(title="Вычитание", control_type="Button"),
            '*': self.dlg.child_window(title="Умножение", control_type="Button"),
            '/': self.dlg.child_window(title="Деление", control_type="Button"),
            '=': self.dlg.child_window(title="Равно", control_type="Button"),
        }

    def actions(self, action: str):
        """
        Метод кликает по кнопкам калькулятора согласно передоной строки кнопок.
        Args:
            action : str
            строка кнопок
        Return:
            None
        """
        for i in action:
            self.calc_buttons[i].click()

    def get_answer(self):
        """
        Метод получает текущий результат вычеслений калькулятора
        :arg:
            None
        :return:
            str
        """
        return self.dlg.child_window(auto_id="158", control_type="Text").window_text()

    def close(self):
        """
        Метод закрывает калькулятор
        :return:
            None
        """
        self.dlg.child_window(title="Закрыть", control_type="Button").click()


'''app = Application(backend="uia").start('calc.exe')
dlg = Desktop(backend="uia").Калькулятор
dlg.print_control_identifiers()
dlg.child_window(title="1").click()
dlg.child_window(title="Сложение").click()
dlg.print_control_identifiers()
dlg.child_window(title="1").click()
'''

