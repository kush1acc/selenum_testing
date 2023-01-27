import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys 
from testlibrary import Testing_library
from customlogger import LogGen
import logging
import time
from time import sleep

class Testing(unittest.TestCase):
    logger=LogGen.loggen()

    def setUp(self):
        self.driver= webdriver.Chrome()
        # self.driver=webdriver.Remote(
        #     command_executor="http://192.168.1.34:4444/wd/hub",
        #     desired_capabilities={
        #         "browserName":"chrome",
        #     })
        self.driver.maximize_window()
    
    def testing_inputbox_checking(self):
        k = Testing_library(self.driver)
        k.go_to_ambdaest_page()
        name = k.name_display()
        time.sleep(2)
        if name==True:
            assert True
        else:
            assert False
        password_display=k.password_display()
        time.sleep(2)
        if password_display==True:
            assert True
        else:
            assert False
        email_display = k.email_display()
        time.sleep(2)
        if email_display==True:
            assert True
        else:
            assert False
        Terms_of_Service = k.Terms_of_Service_display()
        time.sleep(2)
        if Terms_of_Service==True:
            assert True
        else:
            assert False
        phone = k.phone_display()
        time.sleep(2)
        if phone==True:
            assert True
        else:
            assert False
        


        
    def testing_valid_data1(self):
        self.logger=LogGen.loggen()
        self.logger.info("****** testing_valid_data1 ******")
        self.logger.info("****** verifying data with actual data ******")
        k = Testing_library(self.driver)
        k.go_to_ambdaest_page()
        time.sleep(2)
        k.name_input("kush")
        time.sleep(2)
        k.email_input("kushgadewar1111@gmail.com")
        time.sleep(2)
        k.password_input("kush#2001")
        time.sleep(2)
        k.phone_input(8989898989)
        time.sleep(2)
        k.sign_up_input()
        time.sleep(2)
        time.sleep(2)
        email_verification_code_testing_error=self.driver.current_url
        time.sleep(2)
        email_verification_code_testing_error_expected= 'https://accounts.lambdatest.com/email/verify'
        msg1 = "Fail"
        time.sleep(2)
        if email_verification_code_testing_error==email_verification_code_testing_error_expected:
            self.logger.info("****** verifying data with actual data Passed ******")
            assert True
        else:
            self.driver.save_screenshot("G:\kush_selenium_1\screenshots\\"+"testing_valid_data1.png")
            self.logger.error("****** verifying data with actual data Failed ******")
            assert False
        self.driver.close()

    def testing_eamilwithinvali_data(self):
        self.logger.info("****** testing_eamilwithinvali_data ******")
        self.logger.info("****** Testing email with invalid data ******")
        k = Testing_library(self.driver)
        # k.delete_cookies()
        k.redricet()
        time.sleep(2)
        k.name_input("kush")
        time.sleep(2)
        k.email_input("lambda1@gmail.com")
        time.sleep(2)
        k.password_input("kush#2001")
        time.sleep(2)
        k.phone_input(8989898989)
        time.sleep(2)
        k.sign_up_input()
        time.sleep(5)
        email_error= self.driver.find_element(By.XPATH," //*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[2]/form/div[2]/p")
        email_error1 = email_error.text
        email_exist_error = 'This Email is already registered'        
        msg1 = "Fail"
        # error message in case if test case got failed
        # assertEqual() to check equality of first & second value
        time.sleep(5)
        if email_exist_error==email_error1:
            self.logger.info("****** testing_eamilwithinvali_data Passed ******")
            assert True
        else:
            self.driver.save_screenshot("G:\kush_selenium_1\screenshots\\"+"testing_eamilwithinvali_data.png")
            self.logger.error("****** testing_eamilwithinvali_data Falied ******")
            assert False
        print("done")
        self.driver.close()


    def testing_phonewithinvalid_no(self):
        self.logger.info("****** testing_phonewithinvalid_no ******")
        self.logger.info("****** testing_phonewithinvalid_no started ******")
        
        k = Testing_library(self.driver)
        k.delete_cookies()
        k.redricet()
        time.sleep(2)
        k.name_input("kush")
        time.sleep(2)
        k.email_input("kushphonenumber11@gmail.com")
        time.sleep(2)
        k.password_input("kush#2001")
        time.sleep(2)
        k.phone_input(898)
        time.sleep(2)
        k.sign_up_input()
        time.sleep(5)
        phone_actual_error= self.driver.current_url
        phone_expected_error = 'https://accounts.lambdatest.com/email/verify'
        msg1 = "Fail"
        # error message in case if test case got failed
        # assertEqual() to check equality of first & second value
        time.sleep(2)
        if phone_expected_error==phone_actual_error:
            self.logger.info("****** testing_phonewithinvalid_no Passed ******")
            assert True
        else:
            self.driver.save_screenshot("G:\kush_selenium_1\screenshots\\"+"testing_phonewithinvalid_no.png")
            self.logger.error("****** testing_phonewithinvalid_no Failed ******")
            assert False
        print("done")
        self.driver.close()
    
    def testing_passwordofshort_length(self):
        self.logger.info("****** testing_passwordofshort_length  ******")
        self.logger.info("****** testing_passwordofshort_length started ******")
        k = Testing_library(self.driver)
        k.delete_cookies()
        k.redricet()
        time.sleep(2)
        k.name_input("kush")
        time.sleep(2)
        k.email_input("kushpasswordhi11@gmail.com")
        time.sleep(2)
        k.password_input("kush")
        time.sleep(2)
        k.phone_input(8989898989)
        time.sleep(2)
        k.sign_up_input()
        time.sleep(5)
        password_error= self.driver.find_element(By.XPATH," //*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[2]/form/div[3]/p")
        password_error1 = password_error.text
        password_short_error = 'Password should be at least 8 characters long'
        msg1 = "Fail"
        # error message in case if test case got failed
        # assertEqual() to check equality of first & second value
        time.sleep(2)
        if password_short_error==password_error1:
            self.logger.info("****** testing_passwordofshort_length Passed ******")
            assert True
        else:
            self.driver.save_screenshot("G:\kush_selenium_1\screenshots\\"+"testing_passwordofshort_length.png")
            self.logger.error("****** testing_passwordofshort_length Falied ******")
            assert False
        print("done")
        self.driver.close()

    def testing_withoutcheckbox_clicking(self):
        self.logger.info("****** testing_withoutcheckbox_clicking  ******")
        self.logger.info("****** testing_withoutcheckbox_clicking Started ******")
        k = Testing_library(self.driver)
        k.delete_cookies()
        k.redricet()
        time.sleep(2)
        k.name_input("kushraj")
        time.sleep(2)
        k.email_input("kushwithoutcheckingcheckboxhi11@gmail.com")
        time.sleep(2)
        k.password_input("kush#2001")
        time.sleep(2)
        k.phone_input(8989898989)
        time.sleep(2)
        k.sign_up_input()
        time.sleep(5)
        terms_services_actual_error= self.driver.current_url
        terms_services_expected_error = 'https://accounts.lambdatest.com/email/verify'
        msg1 = "Fail"
        # error message in case if test case got failed
        # assertEqual() to check equality of first & second value
        time.sleep(2)
        if terms_services_expected_error==terms_services_actual_error:
            self.logger.info("****** testing_withoutcheckbox_clicking passed ******")
            assert True
        else:
            self.driver.save_screenshot("G:\kush_selenium_1\screenshots\\"+"testing_withoutcheckbox_clicking.png")
            self.logger.error("****** testing_withoutcheckbox_clicking Falied ******")
            assert False
        print("done")
        self.driver.close()


    



        
if __name__ == " __main__":
    unittest.main()