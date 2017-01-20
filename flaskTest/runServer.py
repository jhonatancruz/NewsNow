from flask import Flask, request, render_template, request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pyvirtualdisplay import Display

app= Flask(__name__)


@app.route('/verify')
def verify():
    phone= request.form["phoneNumber"]
    name= request.form["name"]

    #this is where the application logs into twilio
    EMAIL="jcruz3@drew.edu"
    PASSWORD=""
    number=phone

    driver= webdriver.Chrome()
    driver.get("https://www.twilio.com/login")

    email= driver.find_element_by_xpath("//*[@id='email']")
    password= driver.find_element_by_xpath("//*[@id='password']")
    email.send_keys(EMAIL)
    password.send_keys(PASSWORD)

    login =driver.find_element_by_xpath("//*[@id='content']/div[2]/div/form/div[3]/div[1]/button").click()
    #login.click()
    time.sleep(3)
    driver.get("https://www.twilio.com/console/phone-numbers/verified")
    verify= driver.find_element_by_xpath("//*[@id='content']/div[3]/a").click()
    #verify.click()
    time.sleep(2)
    phone=driver.find_element_by_id("PhoneNumber")
    phone.send_keys(number)
    time.sleep(3)
    callMe =driver.find_element_by_xpath("//*[@id='verify-number']/div/div/div[3]/button[2]").click()
    #callMe.click()
    time.sleep(2)
    veriCode= driver.find_element_by_class_name("text-danger")
    #grabs form infor

    return render_template('nextPage.html', name=name, veriCode=veriCode )

@app.route("/", methods=["GET", "POST"])
def index(): #self,phones
    loadingStill= False
    if request.method=="POST":
        verify()

    return render_template("/index.html")

if __name__ =="__main__":
    app.run(debug=True)
