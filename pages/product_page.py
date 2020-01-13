from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import BasketPageLocator


from .login_page import LoginPage
import time


# from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def get_name_item(self):
        field_name_item=self.browser.find_element(*ProductPageLocators.FIELD_NAME_ITEM)
        name_item=field_name_item.text
        return name_item

    def get_price_item(self):
        field_name_item=self.browser.find_element(*ProductPageLocators.FIELD_PRICE_ITEM)
        price_item=field_name_item.text
        return price_item


    def click_to_add_button(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def should_be_add_button(self):
        # self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")
        # assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not presented"
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add button is not presented"

    def verify_name_item(self, _name):
        _name=_name+" has been added to your basket."
        field_name_item = self.browser.find_element(*BasketPageLocator.FIELD_BASKET_ITEM)
        assert _name in field_name_item.text, "Wrong name item"

    def verify_price_basket(self, _price):
        # time.sleep(5)
        field_price_item = self.browser.find_element(*BasketPageLocator.FIELD_BASKET_SUM_PRICE)
        _price="Your basket total is now "+_price
        # print(_price)
        # print(field_price_item.text)
        assert _price in field_price_item.text, "Wrong price basket"


    def should_not_be_success_message(self):
        assert self.is_not_element_present(*BasketPageLocator.FIELD_BASKET_ITEM),"Success message is presented, but should not be"

    def should_not_disappeared_be_success_message(self):
        assert self.is_disappeared(*BasketPageLocator.FIELD_BASKET_ITEM),"Success message is presented, should disapperad"
