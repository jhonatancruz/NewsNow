from flask import Flask, request, render_template, request, session, redirect, url_for
import time
import bs4 as bs
import urllib.request
import requests
from twilio import twiml
from twilio.rest import TwilioRestClient
from twilio.rest import Client
from getNews import news
import os


app= Flask(__name__)

global account_sid
global auth_token
account_sid= "ACecedcfa9c27a1552deaf0f84c4802e80"
auth_token= "03a14d641bb1ac891383065c86f14cc3"
app.secret_key= os.urandom(24)

#TODO: implement a db
#TODO: put account credential in another fille or in DB

#schema
#tables: companies_registered(id, companies), person_id(id, firstname, lastname, phoneNumber, code),

@app.route("/",methods=["GET", "POST"])
def index():
    if request.method=="POST":
        session.pop('phoneNumber', None)
        return verifyPhone()
    return render_template("/index.html")

@app.route("/pickCompany", methods=["GET", "POST"])
def pickCompany():
    if request.method=="POST":
        return render_template("/companies.html")
    else:
        return redirect(url_for('index'))

def verifyPhone():
    try:
        firstName= request.form.get("firstName")
        lastName= request.form.get("lastName")
        phoneNumber= request.form.get("phoneNumber")
        session['phoneNumber']= phoneNumber

        client = Client(account_sid, auth_token)

        validation_request = client.validation_requests \
                                   .create("+1"+phoneNumber,
                                           friendly_name= firstName+" "+lastName)
        code=validation_request.validation_code
        return render_template("verifyCaller.html", code=code, firstName=firstName)
    except Exception as e:
        return("<h1>You are already in the Twilio Verified Numbers!</h1>")

@app.route("/sendNews", methods=["GET", "POST"])
def sendNews():
    if request.method == "POST":
        company= request.form.get("company")
        response=news(str(company))
        headline= response['headlines'][0]
        url=response['urls'][0]

        print(session['phoneNumber'])
        #Twilio messagigng
        client = Client(account_sid, auth_token)
        client.api.account.messages.create(
            to="+1"+session['phoneNumber'],
            from_="+17326246496",
            body= headline+" "+ url)
        return render_template("success.html", company=company)
    else:
        return redirect(url_for('index'))

if __name__ =="__main__":
    app.run(debug=True)
