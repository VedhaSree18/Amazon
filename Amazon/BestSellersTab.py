from selenium.webdriver.common.by import By

class BestSeller:
    def __init__(self,driver):
        self.driver = driver
    Best_Button = (By.XPATH,'(//div[@class="a-section a-spacing-mini _cDEzb_noop_3Xbw5"]/img)[1]')
    def Best_Sel_Fun(self):
        self.driver.find_element(*self.Best_Button).click()
        print('best seller clicked')