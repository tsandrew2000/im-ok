# Download the helper library from https://www.twilio.com/docs/python/install
import os


from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                    body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                    from_='TWILIO_NUMBER',
                    to='+19393976360'
                )

print(message.sid)
