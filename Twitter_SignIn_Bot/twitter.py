from twitterUserInfo import username , password , number
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

class Twitter:
    def __init__(self,username,password,number):
        self.browserProfile =webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option("prefs",{"intl.accept_languages":"en,en_US"})
        self.browser = webdriver.Chrome()
        self.username=username
        self.password=password
        self.number=number

    def signIn(self):
        self.browser.get("https://twitter.com/i/flow/login")
        time.sleep(2)

        usernameInput=self.browser.find_element(By.NAME,"text")
        usernameInput.send_keys(username)
        usernameInput.send_keys(Keys.ENTER)
        time.sleep(2)
        # self.browser.find_elements(By.XPATH,"//div[@role='button']")[-2].click
        
        # if they want to phone number
        numberInput=self.browser.find_element(By.XPATH,"//input")
        numberInput.send_keys(number)
        numberInput.send_keys(Keys.ENTER)
        time.sleep(2)
        
        passwordInput=self.browser.find_element(By.NAME,"password")
        passwordInput.send_keys(password)
        passwordInput.send_keys(Keys.ENTER)


    def search(self,hasthag):
        searchInput=self.browser.find_element(By.XPATH,("//input"))
        searchInput.send_keys(hasthag)
        time.sleep(2)
        searchInput.send_keys(Keys.ENTER)
        time.sleep(2)
       

twitter=Twitter(username,password,number)

twitter.signIn()
twitter.search("borsa")
