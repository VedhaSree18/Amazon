from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from mobiles_tabs import MobilesPage
from BestSellersTab import BestSeller
def get_browser_driver(browser_name):
    if browser_name.lower() == 'chrome':
        # Set up Chrome WebDriver
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_name.lower() == 'firefox':
        # Set up Firefox WebDriver
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser_name.lower() == 'edge':
        # Set up Edge WebDriver
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        raise ValueError("Unsupported browser! Please use 'chrome', 'firefox', or 'edge'.")
    return driver

# Example usage
browser_name = input('please enter browser name:')  # Change this to 'firefox', 'edge', etc.
url = "https://www.amazon.in/"

driver = get_browser_driver(browser_name)
driver.get(url)
driver.implicitly_wait(10)
driver.maximize_window()
time.sleep(5)
mobiles = driver.find_element(By.XPATH,'//a[@href="/mobile-phones/b/?ie=UTF8&node=1389401031&ref_=nav_cs_mobiles"]').click()
time.sleep(3)
mobiles_page = MobilesPage(driver)
mobiles_page.click_example_button()
Dashboard_BestSeller =  driver.find_element(By.CSS_SELECTOR,'a[href="/gp/bestsellers/?ref_=nav_cs_bestsellers"]').click()
best_seller_obj =  BestSeller(driver)
best_seller_obj.Best_Sel_Fun()

# time.sleep(100)

