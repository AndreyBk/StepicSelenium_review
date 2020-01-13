from .base_page import BasePage
from .locators import LoginPageLocator
from .locators import UserPageLocator


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        if self.browser.current_url.find("login") == -1:
            return False
        else:
            return True

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocator.FIELD_LOGIN_EMAIL), "Field login email is not presented"
        assert self.is_element_present(*LoginPageLocator.FIELD_LOGIN_PASS), "Field login password is not presented"
        assert self.is_element_present(*LoginPageLocator.BUTTON_LOGIN), "Field login email is not presented"

        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocator.FIELD_REGISTER_EMAIL), "Field login email is not presented"
        assert self.is_element_present(*LoginPageLocator.FIELD_REGISTER_PASS_1), "Field login email is not presented"
        assert self.is_element_present(*LoginPageLocator.FIELD_REGISTER_PASS_2), "Field login email is not presented"
        assert self.is_element_present(*LoginPageLocator.BUTTON_REGISTER), "Field login email is not presented"

    def register_new_user(self, email, password):
        field_email = self.browser.find_element(*LoginPageLocator.FIELD_REGISTER_EMAIL)
        field_email.send_keys(email)
        field_pass1 = self.browser.find_element(*LoginPageLocator.FIELD_REGISTER_PASS_1)
        field_pass1.send_keys(password)
        field_pass2 = self.browser.find_element(*LoginPageLocator.FIELD_REGISTER_PASS_2)
        field_pass2.send_keys(password)
        button_reg = self.browser.find_element(*LoginPageLocator.BUTTON_REGISTER)
        button_reg.click()
        thanks_message = self.browser.find_element(*UserPageLocator.THANKS_MESSAGE)
        assert "Thanks for registering!" in thanks_message.text, "Registration error"
