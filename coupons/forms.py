from flask_wtf import Form
from wtforms import TextField, FileField, validators

class CouponForm(Form):
    phone_number = TextField('Recipient US Phone Number (ex: 2025551234)', 
        validators=[validators.Required(), validators.regexp(u'[0-9]+')])
    logo_image_url = TextField('Logo Image URL (optional, .png file)')
    serial_number = TextField('Serial Number (optional, ' + \
        'example: 12849480412)')

    def validate(self):
        if not Form.validate(self):
            return False
        if self.logo_image_url.data:
            # ensure at least ends in .png extension if filled in
            if not self.logo_image_url.data[-4:].lower() == '.png':
                return False
        return True

