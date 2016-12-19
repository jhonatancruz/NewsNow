import bs4 as bs
import urllib.request
from twilio import twiml
from twilio.rest import TwilioRestClient

company= input("What company?")
number= input("Give number: ")
ACCOUNT_SID = "AC3bd3a69773f1ea33cb499e04597dcebe"
AUTH_TOKEN = "5fc24bcb11f279efe7e608296bc74093"

sauce= urllib.request.urlopen('https://www.tesla.com/blog').read()
soup= bs.BeautifulSoup(sauce,'lxml')

#print("Top news:",soup.p.text)

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

client.messages.create(
    to="+1"+number,
    from_="+19088458499",
    body= soup.p.text
    )

#the following will ask what companies to grab info from
    #media_url="https://c1.staticflickr.com/3/2899/14341091933_1e92e62d12_b.jpg",
