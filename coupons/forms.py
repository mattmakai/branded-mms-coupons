from flask_wtf import Form
from wtforms import TextField, validators

class CouponForm(Form):
    serial_number = TextField('Serial Number', 
        validators=[validators.Required(), validators.regexp(u'[0-9]+')])

    def validate(self):
        if not Form.validate(self):
            return False
        return True
