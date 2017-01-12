import bs4 as bs
import urllib.request
import requests
from twilio import twiml
from twilio.rest import TwilioRestClient



number= input("what is your number?")
#verify phone number through phone call
ACCOUNT_SID = "AC3bd3a69773f1ea33cb499e04597dcebe"
AUTH_TOKEN = "5fc24bcb11f279efe7e608296bc74093"


#ask for company
company= input("What company?").lower()
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
else:
    print("Try Again")
    company= input("What company?")


client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

client.messages.create(
    to="+1"+number,
    from_="+19088458499",
    body= soup.p.text
    )
