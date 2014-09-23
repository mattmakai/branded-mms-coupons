from flask import request, render_template, jsonify

from . import app
from .forms import CouponForm
from .utils import _create_background_image, _generate_barcode_image


@app.route('/', methods=['GET', 'POST'])
def create_image():
    form = CouponForm()
    if form.validate_on_submit():
        serial_number = form.serial_number.data
        phone_number = form.phone_number.data
        logo_image_url = form.logo_image_url.data
        logo_img = _open_image_url(logo_image_url)
        bg_img = _create_background_image()
        barcode_img = _generate_barcode_image(serial_number)
        finished_coupon = _combine_images_into_coupon(bg_img, logo_img, 
                                                      barcode_img)
    return render_template('create_coupon.html', form=form)
