from selenium.webdriver.common.by import By
from pytest_framework.PageObjects.checkout_confimation import Checkout_Confimration
from pytest_framework.utils.browserutils import BrowserUtils

class ShopPage(BrowserUtils):

    def __init__(self,driver):
        super().__init__(driver)  # used to initilize parent class
        self.driver = driver
        self.shop_link = (By.CSS_SELECTOR, " a[href*='shop']")
        self.product_cards = (By.XPATH, "//div[@class='card h-100']")
        self.checkout_button = (By.CSS_SELECTOR, "a[class*='btn-primary']")


    def add_Product_to_cart(self,product_name):
        self.driver.find_element(*self.shop_link).click()
        products = self.driver.find_elements(*self.product_cards)

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == "Blackberry":
                product.find_element(By.XPATH, "div/button").click()

    def goToCart(self):
        self.driver.find_element(*self.checkout_button).click()
        checkout_conf = Checkout_Confimration(self.driver)
        return checkout_conf
