import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys
from pages.locators import ProductPageLocators
from pages.product_page import ProductPage
from pages.main_page import MainPage
from pages.basket_page import BasketPage


# @pytest.mark.skip
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

    main_page = MainPage(browser, link)
    main_page.open()
    main_page.should_be_basket_button()
    main_page.click_to_basket_button()
    basket_page = BasketPage(browser=main_page.browser, url=main_page.browser.current_url)
    basket_page.open()
    basket_page.not_items_in_basket()
    basket_page.should_be_field_content()
    basket_page.text_basket_is_empty()
