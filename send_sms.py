from twilio.rest import TwilioRestClient

# put your own credentials here
ACCOUNT_SID = "AC3bd3a69773f1ea33cb499e04597dcebe"
AUTH_TOKEN = "5fc24bcb11f279efe7e608296bc74093"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

client.messages.create(
    to="+19082677299",
    from_="+19088458499",
    body="Who are you is the better question"
    #media_url="https://c1.staticflickr.com/3/2899/14341091933_1e92e62d12_b.jpg",
)
