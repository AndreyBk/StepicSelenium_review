import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys
from .pages.locators import ProductPageLocators
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage


# pytest -v --tb=line --language=en test_product_page.py

class TestGuestAddToBasketFromProductPage:
    @pytest.mark.parametrize('link',["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                              pytest.param(
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  marks=pytest.mark.xfail),
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser, link):#+
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_button()
        name_item = page.get_name_item()
        price_item = page.get_price_item()
        page.click_to_add_button()
        page.solve_quiz_and_get_code()
        page.verify_name_item(name_item)
        page.verify_price_basket(price_item)
        # time.sleep(200)

    @pytest.mark.skip
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_button()
        page.click_to_add_button()
        page.solve_quiz_and_get_code()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.skip
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_button()
        page.click_to_add_button()
        page.solve_quiz_and_get_code()
        time.sleep(2)
        page.should_not_disappeared_be_success_message()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):#+
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()
        time.sleep(2)

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):#+
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        product_page = ProductPage(browser, link)
        product_page.open()

        product_page.should_be_basket_button()
        product_page.click_to_basket_button()
        basket_page = BasketPage(browser=product_page.browser, url=product_page.browser.current_url)
        basket_page.open()
        basket_page.not_items_in_basket()
        basket_page.should_be_field_content()
        basket_page.text_basket_is_empty()


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
        self.page = LoginPage(browser, link)
        self.page.open()
        self.page.go_to_login_page()
        email = str(time.time()) + "@fakemail.org"
        self.page.register_new_user(email, "qwertyu1234")
        self.page.should_be_authorized_user()

    def test_user_cant_see_success_message(self):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(self.page.browser, link)
        page.open()
        page.should_be_authorized_user()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self):#+
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(self.page.browser, link)
        page.open()
        page.should_be_authorized_user()
        page.should_be_add_button()
        name_item = page.get_name_item()
        price_item = page.get_price_item()
        page.click_to_add_button()
        page.solve_quiz_and_get_code()
        page.verify_name_item(name_item)
        page.verify_price_basket(price_item)
