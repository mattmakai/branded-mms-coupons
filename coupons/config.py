import os

# General Flask app settings
DEBUG = os.environ.get('DEBUG', None)
SECRET_KEY = os.environ.get('SECRET_KEY', None)
COUPON_SAVE_DIR = os.environ.get('COUPON_SAVE_DIR', None)
QUALIFIED_MEDIA_URL = os.environ.get('QUALIFIED_MEDIA_URL', None)

# Twilio API credentials
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID', None)
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN', None)
TWILIO_NUMBER = os.environ.get('TWILIO_NUMBER', None)
