from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209'
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
@pytest.mark.skip
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
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()

class TestBasketPageFromProductPage():
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_empty_basket()
        basket_page.should_be_text_about_empty_basket()
@pytest.mark.Test_User_Basket
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        email = str(time.time()) + "@fakemail.org"
        password = "12345SayonaraBoi@!"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.go_to_login_page()
        page = LoginPage(browser, browser.current_url)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()
    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
    def test_user_can_add_product_to_basket(self, browser):
        link_1 = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link_1)
        page.open()
        page.should_be_add_to_basket_button()
        page.should_be_success_message()
        page.should_be_correct_item_added()
        page.should_be_correct_basket_summary()