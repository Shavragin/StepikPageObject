from .base_page import BasePage
from .locators import ProductPageLocators

class Product_page(BasePage):
    def go_to_basket(self):
        basket = self.browser.find_element(*ProductPageLocators.BASKET_FORM)
        basket.click()

    def compare_name(self):
        book_name1 = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        name1 = book_name1.text
        book_name2 = self.browser.find_element(*ProductPageLocators.BOOK_NAME_TO_COMPARE)
        name2 = book_name2.text
        assert name1 == name2, "There is different books"

    def compare_costs(self):
        product_cost1 = self.browser.find_element(*ProductPageLocators.COST)
        cost1 = product_cost1.text
        product_cost2 = self.browser.find_element(*ProductPageLocators.COST_TO_COMPARE)
        cost2 = product_cost2.text
        assert cost1 == cost2, "There is different costs"


