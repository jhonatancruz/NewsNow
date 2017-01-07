import bs4 as bs
import urllib.request
import requests
from twilio import twiml
from twilio.rest import TwilioRestClient


number= "9082677299"

#verify phone number through phone call
ACCOUNT_SID = "AC3bd3a69773f1ea33cb499e04597dcebe"
AUTH_TOKEN = "5fc24bcb11f279efe7e608296bc74093"


#ask for company
company= input("What company?")
if input=="tesla":
    sauce= urllib.request.urlopen('https://www.tesla.com/blog').read()
    soup= bs.BeautifulSoup(sauce,'lxml')
else:
    sauce= urllib.request.urlopen('http://www-03.ibm.com/press/us/en/index.wss').read()
    soup= bs.BeautifulSoup(sauce,'lxml')



client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

client.messages.create(
    to="+1"+number,
    from_="+19088458499",
    body= soup.p.text
    )
