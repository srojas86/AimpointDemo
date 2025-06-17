from asyncio import wait_for
import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestPayButtons:
    # First method where the website will be loaded and a product will be added to the shopping cart
    @pytest.fixture(autouse=True)
    def test_addToCart(self, driver):

        # Open the website and maximize window
        driver.get("https://aimpoint.us/")
        driver.maximize_window()

        # Wait for the content to load then click the product
        first_product = WebDriverWait(driver, 120).until(
            expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".product:nth-child(1) .card-image")))
        try:
            first_product.click()
        except NoSuchElementException:
            assert False

        # Once in the product page, add the product to the shopping cart
        add_to_cart = WebDriverWait(driver, 120).until(
            expected_conditions.presence_of_element_located((By.ID, "form-action-addToCart")))
        try:
            add_to_cart.click()
        except NoSuchElementException:
            assert False

    # Second method where the payment buttons will be checked
    def test_buttons(self, test_addToCart, driver):

        # Wait for the content to load then check the ApplePay button
        try:
            apple_pay = WebDriverWait(driver, 120).until(
                expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "apple-pay-button")))
            apple_pay.is_displayed()
            assert True, "Apple Pay button is present"
        except NoSuchElementException:
            assert False, "Apple Pay button is not present"

        # Wait for the content to load then check the ApplePay button
        try:
            g_pay = WebDriverWait(driver, 120).until(
                expected_conditions.presence_of_element_located((By.ID, "gpay-button-online-api-id")))
            g_pay.is_displayed()

            assert True, "Apple Pay button is present"
        except NoSuchElementException:
            assert True, "Apple Pay button is not present"

        driver.quit()