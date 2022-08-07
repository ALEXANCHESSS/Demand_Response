
from Config.config import TestData
from Pages.auth_page import AuthPage
from Tests.test_base import BaseTest


class TestAuth(BaseTest):

    def test_login(self, web_browser):
        self.auth_page = AuthPage(web_browser)
        self.auth_page.login(TestData.LOGIN, TestData.PASSWORD)
        self.auth_page.wait_page_loaded()
        assert self.auth_page.is_visible_logo_DR()

    def test_login_error(self, web_browser):
        self.auth_page = AuthPage(web_browser)
        # self.auth_page.login(TestData.LOGIN, "1234567890")
        body = self.auth_page.get_body_response("https://api.github.com/repos/SergeyPirogov/webdriver_manager")
        print(body["owner"]["login"])










