from .base_page import BasePage
from .locators import BasketPageLocators
class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), 'Basket should be empty, but it is not'
        assert True
    def should_be_text_about_empty_basket(self):
        empty_basket_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET).text
        assert 'Your basket is empty' in empty_basket_text, 'Basket should be empty, but it is not'
        assert True