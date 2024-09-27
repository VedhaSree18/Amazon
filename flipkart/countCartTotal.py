import time
from conftest import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_additems(browser):
    driver = browser
    driver.get('https://www.flipkart.com/')
    time.sleep(3)
    arrow = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'(//div[@class="_3n8fna1ac _3n8fnays _3n8fnan7 _3n8fna1 _3n8fnabm _1i2djtb9 _1i2djt0 _9nihixb7"])[1]')))
    arrow.click()
    wireless = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//div[contains(text(),"Best Truewireless Headphones")]')))
    wireless.click()
    jbl=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//a[contains(text(),"JBL Tune 235NC TWS, Active Noise Cancellation, 40Hr Pla...")]')))
    jbl.click()
    all_tabs = driver.window_handles
    driver.switch_to.window(all_tabs[-1])
    jbl_addcat_button =driver.find_element(By.CSS_SELECTOR,'button[class="QqFHMw vslbG+ In9uk2"]')
    jbl_addcat_button.click()
    flip_home =driver.find_element(By.CSS_SELECTOR,'img[class="W5mR4e"]')
    flip_home.click()
    time.sleep(2)
    login_popup = driver.find_element(By.CSS_SELECTOR,'span[class="_30XB9F"]')
    if login_popup.is_displayed():
        login_popup.click()
    else:
        pass
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'(//div[@class="_3n8fna1ac _3n8fnays _3n8fnan7 _3n8fna1 _3n8fnabm _1i2djtb9 _1i2djt0 _9nihixb7"])[1]'))).click()
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//div[contains(text(),"Best Selling Mobile Speakers")]'))).click()
    govo =WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'(//a[contains(text(),"Mivi Play 5 W Portable Bluetooth Speaker")])[1]')))
    govo.click()
    all_tabs = driver.window_handles
    driver.switch_to.window(all_tabs[-1])
    driver.find_element(By.CSS_SELECTOR,'button[class="QqFHMw vslbG+ In9uk2"]').click()
    time.sleep(4)
    cart_items = driver.find_elements(By.CSS_SELECTOR,'span[class="LAlF6k re6bBo"]')
    lst = []
    for i in cart_items:
        amount = int(float(i.text.strip().replace('₹','').replace(',','')))
        lst.append(amount)
        print(type(amount))
    print(lst)
    new_lst = sum(lst)
    # print(type(new_lst))
    total_cost = driver.find_element(By.XPATH,'(//div[@class="_1Y9Lgu"])[2]/span').text
    total_cost_in_int = int(float(total_cost.strip().replace('₹','').replace(',','')))
    assert new_lst == total_cost_in_int,f'count was not matching'
    print('cart amount was matched with each individual items cost:',new_lst)

