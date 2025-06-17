
import pytest
from selenium import webdriver

@pytest.fixture()
def driver(request):
    driver = webdriver.Firefox()
    yield driver
    # Tear down
    driver.quit()