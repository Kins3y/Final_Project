from .pages.product_page import ProductPage
import pytest
import time

link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209'
@pytest.mark.skip
class TestProductPage():
    @pytest.mark.parametrize('num_link',['0','1','2','3','4','5','6', pytest.param('7', marks=pytest.mark.xfail),'8','9'])
    def test_guest_can_add_product_to_basket(self, browser, num_link):
        link_1 = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num_link}"
        page = ProductPage(browser, link_1)
        page.open()
        page.should_be_correct_url()
        page.should_be_add_to_basket_button()
        page.solve_quiz_and_get_code()
        page.should_be_success_message()
        page.should_be_correct_item_added()
        page.should_be_correct_basket_summary()
        page.should_not_be_success_message()

class TestProductSecondHalf():
    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.solve_quiz_and_get_code()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.solve_quiz_and_get_code()
        page.should_be_add_to_basket_button()
        page.should_not_be_success_form()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()