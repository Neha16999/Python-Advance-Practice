# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC49caeee858347a94dca66907effdf1cc'
auth_token = '0e76ac1028e48638fbeca30940f143b2'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Love your work! This msg is automated by Python',
                              from_='+12082959768',
                              to='+919405150370'
                          )

print(message.sid)
