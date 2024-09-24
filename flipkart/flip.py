import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(4)
    yield driver
    driver.quit()

def search_element(driver):
    driver.get('https://www.flipkart.com')
    searc_bar = driver.find_elment(By.CSS_SELECTOR,'input[class="Pke_EE"]')
    searc_bar.sendkeys('Iphone'+Keys.RETURN)
    time.sleep(4)
    assert 'Iphone' in driver.title
