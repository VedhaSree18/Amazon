import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Amazon.BestSellersTab import BestSeller
@pytest.fixture
def driver():
    # Setup WebDriver
    driver = webdriver.Chrome()
    yield driver
    # Teardown
    driver.quit()

Dashboard_BestSeller =  driver.find_element(By.CSS_SELECTOR,'a[href="/gp/bestsellers/?ref_=nav_cs_bestsellers"]').click()
best_seller_obj =  BestSeller(driver)
best_seller_obj.Best_Sel_Fun()