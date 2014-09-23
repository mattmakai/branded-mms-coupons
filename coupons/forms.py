from flask_wtf import Form
from wtforms import TextField, FileField, validators

class CouponForm(Form):
    phone_number = TextField('Coupon Recipient US Phone Number (ex: 2025551234)', 
        validators=[validators.Required(), validators.regexp(u'[0-9]+')])
    logo_image_url = TextField('Logo Image URL (optional, .png file)',
        validators=[validators.regexp(u'[a-zA-Z0-9\-\.\/]+\.png')])
    serial_number = TextField('Serial Number (optional, ' + \
        'example: 12849480412)', validators=[validators.regexp(u'[0-9]+')])

    def validate(self):
        if not Form.validate(self):
            return False
        return True

