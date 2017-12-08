import json


SECRETS_FILE = 'secrets.json'


# Creating an instance of the Bittrex class with our secrets.json file
with open(SECRETS_FILE) as secrets_file:
    secrets = json.load(secrets_file)
    secrets_file.close()


# Setting up Twilio for SMS alerts
account_sid = secrets['twilio_key']
auth_token = secrets['twilio_secret']
tg_bot_token = secrets.get('tg_bot_token', '')
