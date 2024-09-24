from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://www.amazon.in/')
driver.maximize_window()
driver.implicitly_wait(10)

search_bar = driver.find_element(By.CSS_SELECTOR,'input[id="twotabsearchtextbox"]')
search_bar.send_keys('Iphone13'+Keys.RETURN)

element = driver.find_element(By.XPATH,"(//span[contains(text(),'Apple iPhone 13 (128GB) - Midnight')])[1]")
actual_text = element.text
assert actual_text == 'Apple iPhone 13 (128GB) - Midnight', f'find product was not matched with expected product'
element.click()
all_tabs = driver.window_handles
driver.switch_to.window(all_tabs[-1])
driver.find_element(By.XPATH,'(//input[@id="add-to-cart-button"])[2]').click()
driver.find_element(By.XPATH,'//a[@id="attach-close_sideSheet-link"]').click()  # popup  close
cart_icon = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '(//span[@class="nav-line-2"])[3]')))
cart_icon.click()
cart_subtotal = driver.find_element(By.XPATH,'(//span[@class="a-size-medium a-color-base sc-price sc-white-space-nowrap"])[2]').text
cart_sep = cart_subtotal.strip().replace(',','')
cart_float = float(cart_sep)
print(int(cart_float))
driver.find_element(By.XPATH,'(//input[@class="a-button-input"])[1]').click()
driver.quit()
