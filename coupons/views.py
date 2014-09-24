from flask import request, render_template, jsonify, redirect, url_for

from . import app
from .forms import CouponForm
from .utils import _create_background_image, _generate_barcode_image, \
                   _combine_images_into_coupon, _open_image_file_from_url, \
                   _send_coupon_via_mms

twilio_logo_png_url = 'http://www.twilio.com/packages/company/' + \
                      'img/logos_downloadable_logobrand.png'

@app.route('/', methods=['GET', 'POST'])
def create_image():
    form = CouponForm()
    if form.validate_on_submit():
        serial_number = form.serial_number.data
        phone_number = form.phone_number.data
        logo_image_url = form.logo_image_url.data
        logo_img = _open_image_file_from_url(logo_image_url)
        if not logo_img:
            logo_img = _open_image_file_from_url(twilio_logo_png_url)
        if serial_number:
            barcode_img = _generate_barcode_image(serial_number)
        else:
            barcode_img = _generate_barcode_image()
        coupon_url = _combine_images_into_coupon(logo_img, barcode_img)
        _send_coupon_via_mms(coupon_url, phone_number)        
        redirect(url_for('coupon_confirmation'))
    return render_template('create_coupon.html', form=form)


@app.route('/confirmation/', methods=['GET'])
def coupon_confirmation():
    return render_template('confirmation.html')
