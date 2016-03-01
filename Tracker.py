# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient
import urllib2
import time
from apscheduler.schedulers.background import BackgroundScheduler
#sched = BackgroundScheduler()

# Find these values at https://twilio.com/user/account
account_sid = "AC122c06434e2a90d0a1d24c7046f8518e"
auth_token = "b02ea59bf4796a1f8644c8ec8023d073"
client = TwilioRestClient(account_sid, auth_token)
alreadySent = False
def sendText():
	message = client.messages.create(to="+14403396755", from_="+14407098103",
                                     body="Your Girl Tay Is On Tumblr!")

def check_page():
	#ask the webpage for the info
	while(True):
		global alreadySent
		#wait 10 seconds between checking 
		time.sleep(10)
		page = urllib2.urlopen("http://www.istayontumblr.com/").read()
		page = page.splitlines()
		N=(len(page))
		#find the title element
		for a in range(0, N):
			a = page[a]
    			if '<title>' in a:
        			Title=(str(a))
		Title = Title.strip()
		isSheOn = Title[7]
		#if it's yes send the text!
		if(isSheOn == 'Y'):
			if(alreadySent == False):
				sendText()
				alreadySent = True

		if(isSheOn == 'N'):
			alreadySent = False
			

	
check_page()
#sched.add_job(check_page, 'interval', seconds=10)
#sched.start()

#sched.shutdown()




