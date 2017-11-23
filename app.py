from flask import Flask, request, render_template, request
import time
import bs4 as bs
import urllib.request
import requests
from twilio import twiml
from twilio.rest import TwilioRestClient
from twilio.rest import Client
from getNews import news


app= Flask(__name__)

global account_sid
global auth_token
account_sid= "ACecedcfa9c27a1552deaf0f84c4802e80"
auth_token= "03a14d641bb1ac891383065c86f14cc3"

@app.route("/",methods=["GET", "POST"])
def index(): #self,phones
    if request.method=="POST":
        return verifyPhone()
    return render_template("/index.html")

@app.route("/pickCompany", methods=["GET", "POST"])
def pickCompany():
    if request.method=="POST":
        return render_template("/companies.html")
    return("<h1>Waiting here</h1>")


def verifyPhone():
    firstName= request.form.get("firstName")
    lastName= request.form.get("lastName")
    global phoneNumber
    phoneNumber= request.form.get("phoneNumber")

    client = Client(account_sid, auth_token)

    validation_request = client.validation_requests \
                               .create("+1"+phoneNumber,
                                       friendly_name= firstName+" "+lastName)
    code=validation_request.validation_code
    return render_template("verifyCaller.html", code=code, firstName=firstName)


    # except Exception as e:
    #     return("<h1>There was an error</h1>")
    # return render_template("verifyCaller.html", code=code, firstname=firstname)


@app.route("/sendNews", methods=["GET", "POST"])
def sendNews():
    company= request.form.get("company")
    response=news(str(company))


    #Twilio messagigng
    client = Client(account_sid, auth_token)
    client.api.account.messages.create(
        to="+1"+phoneNumber,
        from_="+17326246496",
        body= response['headlines'][0]
        )
    return render_template("success.html", company=company)


if __name__ =="__main__":
    app.run(debug=True)
