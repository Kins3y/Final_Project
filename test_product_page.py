from .pages.product_page import ProductPage
import pytest
import time

link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
@pytest.mark.product_page
class TestProductPage():
    def test_guest_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_correct_url()
        page.should_be_add_to_basket_button()
        page.solve_quiz_and_get_code()
        page.should_be_success_message()
        page.should_be_correct_item_added()