import time
from pywinauto import Desktop, Application
import pytest
from programs import Calc


@pytest.fixture(scope="function")
def app():
    """
    Фикстура для автотестов. Создает переменную класса управления програмой и передает её в тесты.
    :return:
        app : class Calc
    """
    app = Calc()
    time.sleep(1)
    yield app
    app.close()