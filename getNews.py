import bs4 as bs
import urllib.request
from twilio import twiml
from twilio.rest import TwilioRestClient

# twilioLogin= urllib.request.urlopen("https://www.twilio.com/login")
# auth_handler = urllib.request.HTTPBasicAuthHandler()
# auth_handler.add_password(realm='PDQ Application',
#                           uri='https://mahler:8092/site-updates.py',
#                           user='klem',
#                           passwd='kadidd!ehopper')
# print(twilioLogin.read(500))
#ask for phone number

# create a password manager
# password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
#
# # Add the username and password.
# # If we knew the realm, we could use it instead of None.
# username="jcruz3@drew.edu"
# password= "Mebigunot1!"
# top_level_url = "https://www.twilio.com/login"
# password_mgr.add_password(None, top_level_url, username, password)
#
# handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
#
# # create "opener" (OpenerDirector instance)
# opener = urllib.request.build_opener(handler)
#
# # use the opener to fetch a URL
# opener.open("https://www.twilio.com/login")
#
# # Install the opener.
# # Now all calls to urllib.request.urlopen use our opener.
# urllib.request.install_opener(opener)


number= input("Give your number: ")

#verify phone number through phone call
ACCOUNT_SID = "AC3bd3a69773f1ea33cb499e04597dcebe"
AUTH_TOKEN = "5fc24bcb11f279efe7e608296bc74093"


#ask for company
company= input("What company?")
sauce= requests.get('https://www.tesla.com/blog').read()
soup= bs.BeautifulSoup(sauce,'lxml')


client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

client.messages.create(
    to="+1"+number,
    from_="+19088458499",
    body= soup.p.text
    )
