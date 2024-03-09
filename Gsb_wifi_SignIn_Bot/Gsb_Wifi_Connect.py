from selenium.webdriver.common.by import By
from gsb_wifi_user_info import kullanici_adi,sifre
from selenium import webdriver 
from selenium.common.exceptions import WebDriverException 
import time
from selenium.webdriver.common.keys import Keys
from urllib3.exceptions import MaxRetryError
class GsbWifi:
    def __init__(self,kullanici_adi,sifre) :
        self.browser=webdriver.Chrome()
        self.kullanici_adi=kullanici_adi
        self.sifre=sifre

    def signIn(self):
        
        self.browser.get("http://www.msftconnecttest.com/redirect")
        time.sleep(4)
        kullanici_adi_imput=self.browser.find_element(By.XPATH,"//*[@id='containerall']/form/table/tbody/tr[1]/td[2]/input")
        sifre_input=self.browser.find_element(By.XPATH,"//*[@id='containerall']/form/table/tbody/tr[2]/td[2]/input")

        kullanici_adi_imput.send_keys(self.kullanici_adi)
        sifre_input.send_keys(self.sifre)
        sifre_input.send_keys(Keys.ENTER)

        # console_logs = self.browser.get_log('browser')
        # for log in console_logs:
        #     print(log['level'], log['message'])

        time.sleep(5)

GsbWifi(kullanici_adi,sifre).signIn()