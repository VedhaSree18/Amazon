import time

from conftest import browser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
def test_mobile_pouches(browser):
    browser.get('https://www.flipkart.com')
    browser.implicitly_wait(6)
    search_bar = browser.find_element(By.CSS_SELECTOR,'input[title="Search for Products, Brands and More"]')
    search_bar.send_keys('iqoo mobiles pouches' + Keys.RETURN)
    WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.XPATH,'//a[contains(text(),"IQOO")]')))
    # WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//a[contains(text(),"IQOO")]')))
    list_of_poches = browser.find_elements(By.XPATH,'//a[contains(text(),"IQOO")]')
    time.sleep(4)
    selector = browser.find_element(By.CSS_SELECTOR, 'div[class="Oyj7AF"]')
    action = ActionChains(browser)
    action.click_and_hold(selector).move_by_offset(0, 59).release().perform()
    time.sleep(10)
    value_of_slider = browser.find_element(By.XPATH,'//div[@class="tKgS7w"]/select/option[4]').text
    print(value_of_slider)
    assert '₹400' == value_of_slider, 'value was not moved'

    # for element in list_of_poches:
    #     print(element.text)
    #     if element.text == 'Mobile Back Cover Pouch for IQOO Z9x 5G, IQOO Z9x':
    #         element.click()
    #         break
    # assert len(list_of_poches)>0, 'no elements found with text IQOO'
    # time.sleep(7)
    # all_tabs =browser.window_handles
    # browser.switch_to.window(all_tabs[-1])
    # special_price = browser.find_element(By.CSS_SELECTOR,'div[class="Nx9bqj CxhGGd"]').text.strip().replace('₹','')
    # print(type(special_price))
    # print(special_price)

