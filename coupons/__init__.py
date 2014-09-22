from flask import Flask

app = Flask(__name__)
app.config.from_object('coupons.config')

from . import views
