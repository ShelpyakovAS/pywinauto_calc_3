import time
from pywinauto import Desktop, Application
import pytest
from programs import Calc


@pytest.fixture(scope="function")
def app():
    app = Calc()
    time.sleep(1)
    yield app
    app.close()