from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

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
url = "https://rahulshettyacademy.com/AutomationPractice/"

driver = get_browser_driver(browser_name)
driver.get(url)
driver.implicitly_wait(10)
driver.maximize_window()
mouse =  driver.find_element(By.CSS_SELECTOR,'button[id="mousehover"]')
driver.execute_script('arguments[0].scrollIntoView();',mouse)
mouse.click()
time.sleep(5)