import pytest

from Config.config import TestData
from Pages.auth_page import AuthPage


@pytest.mark.usefixtures("web_browser")
class BaseTest:
    pass
