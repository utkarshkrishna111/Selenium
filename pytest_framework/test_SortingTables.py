import time
from selenium import webdriver
from selenium.webdriver import ActionChains
#Chrome Driver
from selenium.webdriver.chrome.service import Service
#By contains locators
from selenium.webdriver.common.by import By

def test_sort(browserInstance):
    driver = browserInstance
    browerSortveggies = []
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers/")
    
    driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

    veggieWebelement = driver.find_elements(By.XPATH, "//tr/td[1]")



    for ele in veggieWebelement:
        browerSortveggies.append(ele.text)

    # to create a copy of the list
    original_browerSortveggies = browerSortveggies.copy()
    browerSortveggies.sort()

    print(browerSortveggies)

    assert browerSortveggies == original_browerSortveggies

