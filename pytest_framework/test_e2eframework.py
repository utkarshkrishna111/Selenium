import json
import pytest

from selenium import webdriver

#chrome driver
from selenium.webdriver.chrome.service import Service
#-- Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pytest_framework.PageObjects.login import LoginPage

test_data_path = '../data/test_e2eframework.json'
with open(test_data_path) as file:
    test_data = json.load(file)
    test_list = test_data["data"]

@pytest.mark.smoke
#pytest.mark.parametrize : Passes one by one the items in the list
@pytest.mark.parametrize("test_list_item",test_list)
def test_e2e(browserInstance,test_list_item):
    driver = browserInstance
    loginPage = LoginPage(driver)
#print(loginPage.getTitle())
    shop_page = loginPage.login(test_list_item["userEmail"],test_list_item["userPassword"])
    shop_page.add_Product_to_cart(test_list_item["productName"])
#print(shop_page.getTitle())
    #  //a[contains(@href,'shop')]    a[href*='shop']
    checkout_confirmation = shop_page.goToCart()
#print(checkout_confirmation.getTitle())
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address("ind")
    checkout_confirmation.validate_order()
    
#pytest -n 2 is used to run multiple tests together. pytest-xdist is to be installed
#py.test --html reports/reports.html : command for generating reports


# pytest -n 2 -m smoke --browser_name firefox --html=reports/report.html





    
    
