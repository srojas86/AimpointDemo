import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.conftest import driver


class TestProductsFlow:

    # First method where the website will be loaded and a product will be added to the shopping cart
    @pytest.mark.usefixtures("driver")
    def test_add_product(self, driver, base_url):
        # Open the website and maximize window
        driver.get(base_url)
        driver.maximize_window()

        # Wait for the content to load then click the product
        try:
            first_product = WebDriverWait(driver, 10).until(
                expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".product:nth-child(1) .card-image")))
            first_product.click()
        except NoSuchElementException:
            assert False

        # Once in the product page, add the product to the shopping cart
        try:
            add_to_cart = WebDriverWait(driver, 10).until(
                expected_conditions.presence_of_element_located((By.ID, "form-action-addToCart")))
            add_to_cart.click()
        except NoSuchElementException:
            assert False

    # Second method where the payment buttons will be checked

    def test_buttons(self, driver):
        # Wait for the content to load then check the ApplePay button
        try:
            apple_pay = WebDriverWait(driver, 10).until(
                expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "apple-pay-button")))
            assert apple_pay is not None
        except NoSuchElementException:
            assert False

        # Wait for the content to load then check the GooglePay button
        try:
            g_pay = WebDriverWait(driver, 10).until(
                expected_conditions.presence_of_element_located((By.ID, "gpay-button-online-api-id")))
            assert g_pay is not None
        except NoSuchElementException as e:
            assert False

        driver.quit()