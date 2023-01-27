import time
import requests
import re
import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
# import unittest

# launchin browser
# def webdriver_run():
#     opts = Options()
#     driver = webdriver.Chrome(options=opts, executable_path='chromedriver_win32')
#     return driver

class Testing_library:
    def __init__(self,driver):
        self.driver =driver
#  going to the login page
    def go_to_ambdaest_page(self):
        
        self.driver.get(" https://www.lambdatest.com/webpage")
        time.sleep(2)
        signup_button = self.driver.find_element(By.XPATH, '//a[text()="Sign Up"]')
        signup_button.click()

    # diplay chcking code 

    def name_display(self):
        
        name = self.driver.find_element(By.XPATH,"//input[@name='name']")
        if name.is_displayed():
            return True

        

    def email_display(self):
        
        email = self.driver.find_element(By.XPATH,"//input[@name='email']")
        if email.is_displayed():
            return True

    def password_display(self):
        
        password = self.driver.find_element(By.XPATH,"//input[@name='password']")
        if password.is_displayed():
            return True

    def phone_display(self):
        
        phone = self.driver.find_element(By.XPATH,"//input[@name='phone']")
        if phone.is_displayed():
            return True

    def Terms_of_Service_display(self):
        
        Terms_of_Service = self.driver.find_element(By.XPATH, '//a[text()="Terms of Service"]')
        if Terms_of_Service.is_displayed():
            return True


    #  validation function of form

    def name_input(self,name1):
        
        name = self.driver.find_element(By.XPATH,"//input[@name='name']")
        name.send_keys(name1)

    def email_input(self,email1):
        
        email = self.driver.find_element(By.XPATH,"//input[@name='email']")
        email.send_keys(email1)

    def password_input(self,password1):
        
        password = self.driver.find_element(By.XPATH,"//input[@name='password']")
        password.send_keys(password1)

    def phone_input(self,phone1):
           
        phone = self.driver.find_element(By.XPATH,"//input[@name='phone']")
        phone.send_keys(phone1)

    def Terms_of_Service(self):
        
        Terms_of_Service = self.driver.find_element(By.XPATH, '//a[text()="Terms of Service"]')
        Terms_of_Service.click()

    def sign_up_input(self):
        sign_up = self.driver.find_element(By.XPATH,"//button[text()='FREE SIGN UP']")
        sign_up.click()
    
    def redricet_link(self):
        redricet = self.driver.current_url
        return redricet

    def redricet(self):
        redricet = self.driver.get("https://accounts.lambdatest.com/register")

    def delete_cookies(self):
        redricet = self.driver.delete_all_cookies()

# class TestStringMethods():
    # def __init__(self,driver,module):
    #     self=module
    #     self.driver =driver

    # test function to test equality of two value
    # def email_existing_testing(self):
    #     email_error= self.driver.find_element(By.XPATH," //*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[2]/form/div[2]/p")
    #     email_error1 = email_error.text
    #     email_exist_error = 'This Email isalready registered'
    #     msg1 = "This Email is already registered to the site"

    #     firstValue = email_exist_error
    #     secondValue = email_error.text
    #     # error message in case if test case got failed
    #     message = "First value and second value are not equal !"
    #     # assertEqual() to check equality of first & second value
    #     self.assertEqual(firstValue, secondValue, msg1)

    # def password_length_testing(self):
    #     password_error= self.driver.find_element(By.XPATH," //*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[2]/form/div[3]/p")
    #     password_error1 = password_error.text
    #     password_short_error = 'This Email isalready registered'
    #     msg1 = "There is error in passwrd"

    #     # error message in case if test case got failed
    #     # assertEqual() to check equality of first & second value
    #     self.assertEqual(password_short_error, password_error1, msg1)