from selenium.webdriver.common.by import By
from instagramUserInfo import email,password
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

class Instagram:
    def __init__(self,email,password) :
        self.browser=webdriver.Chrome()
        self.email=email
        self.password=password


    def signIn(self):
        self.browser.get("https://www.instagram.com/")
        time.sleep(1)
        emailInput=self.browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput=self.browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[2]/div/label/input")

        emailInput.send_keys(self.email)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(8)

        # if self.browser.find_element(By.CLASS_NAME,"cmbtv"):

        #     simdi_degil=self.browser.find_element(By.CLASS_NAME,"cmbtv")
        #     simdi_degil.find_element(By.TAG_NAME,"button").click
        #     time.sleep(5)

        # if self.browser.find_element(By.XPATH,"//*[@id='mount_0_0_Ti']/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]"):

        #     bildirim=self.browser.find_element(By.XPATH,"//*[@id='mount_0_0_Ti']/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
        #     bildirim.click


    def followers(self):
        self.browser.get("https://www.instagram.com/youraccount/following")

        time.sleep(30)

        followers=self.browser.find_element(By.XPATH,"div[role=dialog]").find_element(By.XPATH,"//*[@id='mount_0_0_Gk']/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div/div[1]")

        for user in followers:
            link=user.find_element(By.XPATH,"//*[@id='f312d72c5891558']/div/div/span/a").get_attribute("href")
            print(link)


    def follow(self):
        self.browser.get("https://www.instagram.com/youraccount")

        time.sleep(3)

        follow=self.browser.find_element(By.XPATH,"//*[@id='mount_0_0_93']/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/div[3]/div/div/button/div")
        follow.click()

instagram=Instagram(email,password)
instagram.signIn()
instagram.followers()
# instagram.followers()
# instagram.followers()







