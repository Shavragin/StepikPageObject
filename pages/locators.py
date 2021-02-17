from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR,"#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR,"login_form")
    REGISTER_FORM = (By.CSS_SELECTOR,"register_form")


class ProductPageLocators():
    BASKET_FORM = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    BOOK_NAME_TO_COMPARE = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    COST = (By.XPATH,'//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')
    COST_TO_COMPARE = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')