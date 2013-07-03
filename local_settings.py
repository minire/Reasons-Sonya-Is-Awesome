'''
Configuration Settings

Includes keys for Twilio, etc.  Second stanza intended for Heroku deployment.
'''

# Uncommet to configure in file.
ACCOUNT_SID = "AC11759b18e54ca436f11ac4fc2dbf07db" 
AUTH_TOKEN = "884317e08c7a43afc8c50038ba8c2259"
SONYA_APP_SID = "APd3c4f0a1cd8d4a64afa38d5075f10bcc"
SONYA_CALLER_ID = "12696723560"


# Begin Heroku configuration - configured through environment variables.
import os
ACCOUNT_SID = os.environ['ACCOUNT_SID']
AUTH_TOKEN = os.environ['AUTH_TOKEN']
SONYA_APP_SID = os.environ['SONYA_APP_SID']
SONYA_CALLER_ID = os.environ['SONYA_CALLER_ID']
