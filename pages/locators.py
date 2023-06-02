from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form > button')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1)')
    ITEM_NAME = (By.CSS_SELECTOR, 'div.col-sm-6.product_main > h1')