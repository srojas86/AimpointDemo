import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def driver(request):
    driver = webdriver.Firefox()
    yield driver

@pytest.fixture(autouse=True)
def base_url(driver):
    main_website = "https://aimpoint.us/"
    yield main_website


@pytest.fixture()
def teardown(driver):
    driver.quit()
