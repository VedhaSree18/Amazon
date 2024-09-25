import random

from conftest import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# def test_findingDashboardSliderlength(browser):
#     driver = browser
#     driver.get('https://www.flipkart.com/')
#     driver.implicitly_wait(5)
#     slider_elements=driver.find_elements(By.XPATH,'//div[@class="_3bzdSa"]/div')
#     print(len(slider_elements))
#     for i in slider_elements:
#         print(i.screenshot(random.randint[1,4]))
#     time.sleep(4)
def test_list_of_items(browser):
    driver = browser
    driver.get('https://www.flipkart.com/')
    driver.implicitly_wait(5)
    items = driver.find_elements(By.XPATH,'//div[@class="tLbyDf"]/div[@class="_25HC_u"]/div/div/div/a/div/div/div[2]/div')
    print(len(items))
    for i in items:
        print(i.text)
    time.sleep(5)