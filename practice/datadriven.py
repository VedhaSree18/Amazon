import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import os
@pytest.fixture(params=pd.read_csv('C:\\Users\\Venkata.M\\Downloads\\sample_data.csv').to_dict('records'))
def data(request):
    return request.param

@pytest.fixture
def driver():
    # Set up the WebDriver
    driver = webdriver.Chrome()  # Or use Firefox(), etc.
    yield driver
    driver.quit()

def test_login(driver, data):
    # Navigate to the login page
    driver.get("https://practicetestautomation.com/practice-test-login/")  # Replace with the actual login page URL

    # Find and fill in the username field
    username_field = driver.find_element(By.ID, "username")  # Replace with the actual field ID or selector
    username_field.send_keys(data['Username'])

    # Find and fill in the password field
    password_field = driver.find_element(By.ID, "password")  # Replace with the actual field ID or selector
    password_field.send_keys(data['Password'])

    # Submit the form
    password_field.send_keys(Keys.RETURN)

    # Add assertions or checks here as needed
    # Example: Check if login was successful
    # assert "Dashboard" in driver.title  # Replace with an actual check based on your application
