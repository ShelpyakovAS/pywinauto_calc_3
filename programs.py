from pywinauto import Desktop, Application
import random


class Calc:

    def __init__(self):
        self.app = Application(backend="uia").start('calc.exe')
        self.dlg = Desktop(backend="uia").Калькулятор
        self.calc_button = {
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
        for i in action:
            self.calc_button[i].click()

    def get_answer(self):
        return self.dlg.child_window(auto_id="158", control_type="Text").window_text()

    def close(self):
        self.dlg.child_window(title="Закрыть", control_type="Button").click()


'''app = Application(backend="uia").start('calc.exe')
dlg = Desktop(backend="uia").Калькулятор
dlg.print_control_identifiers()
dlg.child_window(title="1").click()
dlg.child_window(title="Сложение").click()
dlg.print_control_identifiers()
dlg.child_window(title="1").click()
'''
