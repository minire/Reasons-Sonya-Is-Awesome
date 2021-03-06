'''
Configuration Settings

Includes keys for Twilio, etc.  Second stanza intended for Heroku deployment.
'''

# Uncommet to configure in file.
ACCOUNT_SID = "ACnnnnnnnnnnnnnnnnnnnnnnnnnnnnn" 
AUTH_TOKEN = "xxxxxxxxxxxxxxxxxxxxxxxx"
SONYA_APP_SID = "APcccccccccccc"
SONYA_CALLER_ID = "12456789032"


# Begin Heroku configuration - configured through environment variables.
import os
ACCOUNT_SID = os.environ['ACCOUNT_SID']
AUTH_TOKEN = os.environ['AUTH_TOKEN']
SONYA_APP_SID = os.environ['SONYA_APP_SID']
SONYA_CALLER_ID = os.environ['SONYA_CALLER_ID']
