import os
from os import environ

basedir = os.path.abspath(os.path.dirname(__file__))

def get_env_setting(setting):
    """ Get the environment setting or return exception """
    try:
        var_set = environ[setting]
        if var_set == 'true' or var_set == 'True':
            return True
        elif var_set == 'false' or var_set == 'False':
            return False
        return var_set
    except KeyError:
        error_msg = "Set the %s env variable" % setting
        raise Exception(error_msg)


# General Flask app settings
DEBUG = get_env_setting('DEBUG')
SECRET_KEY = get_env_setting('SECRET_KEY')
COUPON_SAVE_DIR = get_env_setting('COUPON_SAVE_DIR')
QUALIFIED_MEDIA_URL = get_env_setting('QUALIFIED_MEDIA_URL')

# Twilio API credentials
TWILIO_ACCOUNT_SID = get_env_setting('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = get_env_setting('TWILIO_AUTH_TOKEN')
TWILIO_NUMBER = get_env_setting('TWILIO_NUMBER')
