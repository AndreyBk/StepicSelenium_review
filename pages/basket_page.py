from selenium.common.exceptions import NoSuchElementException
import math
from selenium.common.exceptions import NoAlertPresentException  # в начале файла
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from .locators import BasketPageLocator
from .base_page import BasePage


# import BasePage


class BasketPage(BasePage):

    def should_be_field_content(self):
        # self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")
        # assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not presented"
        assert self.is_element_present(*BasketPageLocator.FIELD_CONT_BASKET), "Field content is not presented"

    def text_basket_is_empty(self):
        field_content = self.browser.find_element(*BasketPageLocator.FIELD_CONT_BASKET)
        assert "Your basket is empty" in field_content.text, "Text content basket not empty"

    def not_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocator.FIELD_BASKET_ITEM)