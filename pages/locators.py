from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_EMAIL_ADDRESS = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_PASSWORD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_PASSWORD_CONFIRM = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '[name="registration_submit"]')

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form > button')
    SUCCESS_FORM = (By.CSS_SELECTOR, '#messages > div:nth-child(1)')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    ITEM_NAME = (By.CSS_SELECTOR, 'div.col-sm-6.product_main > h1')
    ITEM_PRICE = (By.CSS_SELECTOR,'div.col-sm-6.product_main > p.price_color')
    BASKET_SUMMARY = (By.CSS_SELECTOR, '#messages > div:nth-child(3) > div > p > strong')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    SHOW_BASKET_BUTTON = (By.CSS_SELECTOR, 'span > a')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, '[class="basket-items"]')
    EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner > p')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")