from flask import Flask, request, render_template, request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pyvirtualdisplay import Display
import bs4 as bs
import urllib.request
import requests
from twilio import twiml
from twilio.rest import TwilioRestClient

app= Flask(__name__)

@app.route("/",methods=["GET", "POST"])
def index(): #self,phones
    if request.method=="POST":
        return verifyPhone()
    return render_template("/index.html")

@app.route("/pickCompany", methods=["GET", "POST"])
def pickCompany():
    if request.method=="POST":
        return render_template("/companies.html")

    return render_template("/nextPage.html")

def verifyPhone():

    EMAIL="jcruz3@drew.edu"
    PASSWORD="Mebigunot1!"

    number=input("what is your number?")
    driver= webdriver.PhantomJS()
    driver.set_window_size(1124, 850) # set browser size.
    driver.get("https://www.twilio.com/login")

    email= driver.find_element_by_xpath("//*[@id='email']")
    password= driver.find_element_by_xpath("//*[@id='password']")
    email.send_keys(EMAIL)
    password.send_keys(PASSWORD)

    login =driver.find_element_by_xpath("//*[@id='content']/div[2]/div/form/div[3]/button[1]").click()
    print("logged in")
    time.sleep(3)
    driver.get("https://www.twilio.com/console/phone-numbers/verified")
    print("inside verified numbers tab")

    verify= driver.find_element_by_xpath("//*[@id='content']/div[3]/div[1]/a/span/i[2]").click()
    # verify= driver.find_element_by_xpath("//*[@id='content']/div[3]/a").click()
    time.sleep(2)
    phone=driver.find_element_by_id("PhoneNumber")
    # time.sleep(2)
    phone.send_keys(number)
    print("about to call")
    # time.sleep(5)
    callMe =driver.find_element_by_xpath("//*[@id='verify-number']/div/div/div[3]/button[2]").click()
    #callMe.click()
    time.sleep(3)
    veriCode= driver.find_element_by_class_name("text-danger")
    print("Put the following digits on your phone when they call:"+ veriCode.text)
    driver.quit()

    return render_template('nextPage.html', name=name, veriCode=veriCode )


@app.route("/verifyCompany", methods=["GET", "POST"])
def verifyCompany():
    if request.method=="POST":
        companyName= request.form["company"]

        ACCOUNT_SID = "AC3bd3a69773f1ea33cb499e04597dcebe"
        AUTH_TOKEN = "5fc24bcb11f279efe7e608296bc74093"

        #ask for company
        company= companyName
        if company=="tesla":
            sauce= urllib.request.urlopen('https://www.tesla.com/blog').read()
            soup= bs.BeautifulSoup(sauce,'lxml')
        elif company=="verizon":
            sauce= urllib.request.urlopen('http://www.verizon.com/about/news').read()
            soup= bs.BeautifulSoup(sauce,'lxml')
        elif company=="apple":
            sauce= urllib.request.urlopen('http://www.apple.com/newsroom/').read()
            soup= bs.BeautifulSoup(sauce,'lxml')
        elif company=="samsung":
            sauce= urllib.request.urlopen('https://news.samsung.com/us/').read()
            soup= bs.BeautifulSoup(sauce,'lxml')
        elif company=="microsoft":
            sauce= urllib.request.urlopen('http://news.microsoft.com/#sm.00zysa8e1ej9dds109q20m4ljtlni').read()
            soup= bs.BeautifulSoup(sauce,'lxml')


        client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

        client.messages.create(
            to="+1"+number,
            from_="+19088458499",
            body= soup.p.text
            )
        return render_template("success.html")


if __name__ =="__main__":
    app.run(debug=True)
