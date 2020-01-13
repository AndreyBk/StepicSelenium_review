from selenium.webdriver.common.by import By


# class MainPageLocators():
#     LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
# LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.XPATH, "//button[@value='Add to basket']")
    FIELD_NAME_ITEM = (By.XPATH, "//h1")
    FIELD_PRICE_ITEM = (By.XPATH, "//p[@class='price_color'][1]")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_BASKET = (By.CSS_SELECTOR, ".btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocator():
    FIELD_CONT_BASKET = (By.XPATH, "//p")
    FIELD_BASKET_ITEM = (By.XPATH, "//div[@class='alertinner '][1]")
    FIELD_BASKET_SUM_PRICE = (By.XPATH, "//div[@class='alertinner ']/p")

class LoginPageLocator():
    FIELD_LOGIN_EMAIL = (By.XPATH, "//input[@name='login-username']")
    FIELD_LOGIN_PASS = (By.XPATH, "//input[@name='login-password']")
    BUTTON_LOGIN = (By.XPATH, "//button[@name='login_submit']")

    FIELD_REGISTER_EMAIL = (By.XPATH, "//input[@name='registration-email']")
    FIELD_REGISTER_PASS_1 = (By.XPATH, "//input[@name='registration-password1']")
    FIELD_REGISTER_PASS_2 = (By.XPATH, "//input[@name='registration-password2']")
    BUTTON_REGISTER = (By.XPATH, "//button[@name='registration_submit']")

class UserPageLocator():
    THANKS_MESSAGE = (By.XPATH, "//div[@class='alertinner wicon']")


