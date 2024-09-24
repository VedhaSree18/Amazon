from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import browser

def test_search_element(browser):
    browser.get('https://www.flipkart.com')
    browser.implicitly_wait(4)
    search_bar = browser.find_element(By.CSS_SELECTOR,'input[class="Pke_EE"]')
    search_bar.send_keys('Iphone'+Keys.RETURN)
    WebDriverWait(browser,10).until(EC.title_contains('phone'))
    phones_ = browser.find_elements(By.CSS_SELECTOR,'div[class="KzDlHZ"]')
    phones_[1].click()
    time.sleep(4)
    all_tabs= browser.window_handles
    browser.switch_to.window(all_tabs[-1])
    browser.find_element(By.CSS_SELECTOR,'button[class="QqFHMw vslbG+ _3Yl67G _7Pd1Fp"]').click()  # buy BUTTON
    time.sleep(4)
    input("please do manual step and hit enter")   # it will wait till input given by user and after used this please use -s while run command
    # after this delivery button


