from Base.base import WebPage
from Base.elements import WebElement
from Config.config import TestData


class AuthPage(WebPage):

    email = WebElement(xpath="//input[@type='text']")
    password = WebElement(xpath="//input[@type='password']")
    button = WebElement(class_name='Auth__Login-akhk15-9.dheurx')
    logo_DR = WebElement(css_selector=".TopMenu__Logo-zvv1mz-6.cSDUFq")

    def __init__(self, web_browser, url=''):
        if not url:
            url = TestData.URL_MAIN
        super().__init__(web_browser, url)

    def login(self, login, password):
        """Authorization on the site"""
        self.email.send_keys(login)
        self.password.send_keys(password)
        self.button.click()

    def is_visible_logo_DR(self):
        """Is the logo visible?"""
        return self.logo_DR.is_visible()




