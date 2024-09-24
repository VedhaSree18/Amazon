import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# Fixture to handle browser setup and teardown
@pytest.fixture(params=["chrome", "firefox", "edge"])
def driver(request):
    browser_name = request.param
    if browser_name == 'chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_name == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser_name == 'edge':
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        raise ValueError("Unsupported browser! Please use 'chrome', 'firefox', or 'edge'.")

    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


# Test function for the Amazon navigation
@pytest.mark.parametrize('driver', ["chrome", "firefox", "edge"], indirect=True)
def test_amazon_navigation(driver):
    url = "https://www.amazon.in/"
    driver.get(url)

    # Clicking on the Mobiles link
    mobiles = driver.find_element(By.XPATH,
                                  '//a[@href="/mobile-phones/b/?ie=UTF8&node=1389401031&ref_=nav_cs_mobiles"]')
    mobiles.click()
    time.sleep(3)

    # Interact with MobilesPage object
    # mobiles_page = MobilesPage(driver)
    # mobiles_page.click_example_button()

    # Clicking on Best Sellers tab
    # best_sellers = driver.find_element(By.CSS_SELECTOR, 'a[href="/gp/bestsellers/?ref_=nav_cs_bestsellers"]')
    # best_sellers.click()
    #
    # # Interact with BestSeller object
    # best_seller_obj = BestSeller(driver)
    # best_seller_obj.Best_Sel_Fun()

    # Add assertions for validation (as an example)
    # assert "bestsellers" in driver.current_url, "Best Sellers page did not load correctly"
    print('mobiles was redirected')