# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient
import urllib2
from apscheduler.schedulers.background import BackgroundScheduler

sched = BackgroundScheduler()

def check_page():
	page = urllib2.urlopen("http://www.istayontumblr.com/").read()
	print page

sched.add_job(check_page, 'interval', seconds=10)
sched.start()

sched.shutdown()

#Check isTayOnTumblr.com
page = urllib2.urlopen("http://www.istayontumblr.com/").read()
print page
 
# Find these values at https://twilio.com/user/account
account_sid = "AC122c06434e2a90d0a1d24c7046f8518e"
auth_token = "b02ea59bf4796a1f8644c8ec8023d073"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(to="+14403396755", from_="+14407098103",
                                     body="Your Girl Tay Is On Tumblr!")
