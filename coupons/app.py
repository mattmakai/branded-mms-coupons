from flask import Flask, request, render_template, redirect, url_for

from .forms import CouponForm
#from .utils import generate_barcode_image, combine_images_into_coupon, \
#                   open_image_file_from_url, send_coupon_via_mms

twilio_logo_png_url = 'http://www.twilio.com/packages/company/' + \
                      'img/logos_downloadable_logobrand.png'

app = Flask(__name__, static_url_path='/static')
app.config.from_pyfile('config.py')


@app.route('/', methods=['GET', 'POST'])
def create_coupon():
    return 'stub'


@app.route('/confirmation/', methods=['GET'])
def coupon_confirmation():
    return 'stub'

