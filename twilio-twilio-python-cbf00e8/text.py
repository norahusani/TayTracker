# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient
 
# Find these values at https://twilio.com/user/account
account_sid = "AC122c06434e2a90d0a1d24c7046f8518e"
auth_token = "b02ea59bf4796a1f8644c8ec8023d073"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(to="+14403396755", from_="+14407098103",
                                     body="Your Girl Tay Is On Tumblr!")