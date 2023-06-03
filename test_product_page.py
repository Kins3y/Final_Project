from .pages.product_page import ProductPage
import pytest
import time

#link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=offer7'
@pytest.mark.product_page
class TestProductPage():
    @pytest.mark.parametrize('num_link',['0','1','2','3','4','5','6', pytest.param('7', marks=pytest.mark.xfail),'8','9'])
    def test_guest_can_add_product_to_basket(self, browser, num_link):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num_link}"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_correct_url()
        page.should_be_add_to_basket_button()
        page.solve_quiz_and_get_code()
        page.should_be_success_message()
        page.should_be_correct_item_added()
        page.should_be_correct_basket_summary()