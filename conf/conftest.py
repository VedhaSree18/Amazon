import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# Fixture to initialize browser based on the parameter
@pytest.fixture(params=["chrome", "firefox"], scope="function")
def browser(request):
    browser_choice = request.param

    if browser_choice == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_choice == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise ValueError(f"Browser '{browser_choice}' is not supported")

    driver.maximize_window()
    yield driver
    driver.quit()
