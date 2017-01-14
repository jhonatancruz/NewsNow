from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

EMAIL="jcruz3@drew.edu"
PASSWORD=""

number= input("what is your number?")
driver= webdriver.Chrome()
driver.get("https://www.twilio.com/login")

email= driver.find_element_by_xpath("//*[@id='email']")
password= driver.find_element_by_xpath("//*[@id='password']")
email.send_keys(EMAIL)
password.send_keys(PASSWORD)

login =driver.find_element_by_xpath("//*[@id='content']/div[2]/div/form/div[3]/div[1]/button").click()
#login.click()
time.sleep(5)
driver.get("https://www.twilio.com/console/phone-numbers/verified")
verify= driver.find_element_by_xpath("//*[@id='content']/div[3]/a").click()
#verify.click()
time.sleep(2)
phone=driver.find_element_by_id("PhoneNumber")
phone.send_keys(number)
time.sleep(5)
callMe =driver.find_element_by_xpath("//*[@id='verify-number']/div/div/div[3]/button[2]").click()
#callMe.click()
time.sleep(2)
veriCode= driver.find_element_by_class_name("text-danger")
print("Put the following digits on your phone when they call:"+ veriCode.text)
driver.quit()
