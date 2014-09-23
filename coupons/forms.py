from flask_wtf import Form
from wtforms import TextField, FileField, validators

class CouponForm(Form):
    serial_number = TextField('Serial Number (ex: 12849129480412)', 
        validators=[validators.Required(), validators.regexp(u'[0-9]+')])
    phone_number = TextField('US Phone Number (ex: 2025551234)', 
        validators=[validators.Required(), validators.regexp(u'[0-9]+')])
    logo_image_url = TextField('Logo Image URL (.png)',
        validators=[validators.Required(), 
        validators.regexp(u'[a-zA-Z0-9\-\.\/]+\.png')])

    def validate(self):
        if not Form.validate(self):
            return False
        return True

