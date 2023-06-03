from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_work_basket_page(self):
        self.should_be_correct_url()
        self.should_be_add_to_basket_button()
        self.should_be_success_message()
        self.should_be_correct_item_added()
        self.should_be_correct_basket_summary()

    def should_be_correct_url(self):
        newyear_promo = '?promo=offer'
        assert newyear_promo in self.browser.current_url, "This is incorrect URL for NewYear promo"
        assert True
    def should_be_add_to_basket_button(self):
        link = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        link.click()
    def should_be_success_message(self):
        sm = self.browser.find_element(*ProductPageLocators.SUCCESS_FORM)
        assert sm.is_displayed, 'Success_message is not presented'
        assert True
    def should_be_correct_item_added(self):
        message_text = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert self.browser.find_element(*ProductPageLocators.ITEM_NAME).text == message_text, 'Wrong ITEM_NAME'
        assert True
    def should_be_correct_basket_summary(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        basket_summary = self.browser.find_element(*ProductPageLocators.BASKET_SUMMARY).text
        assert item_price == basket_summary, 'item_price not equals basket_summary'
        assert True
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), 'Success message is presented, but should not be'

    def should_not_be_success_form(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_FORM), 'Success form used to disappear'
