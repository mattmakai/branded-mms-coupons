from flask import request, render_template, jsonify

from . import app
from .forms import CouponForm
from .utils import _create_background_image, _generate_barcode_image


@app.route('/', methods=['GET', 'POST'])
def create_image():
    form = CouponForm()
    if form.validate_on_submit():
        logo_file = request.files['file']
        try:
            img = Image.open(logo_file)
        except:
            # cannot open image
            render_template('invalid_file.html')
        serial_number = form.serial_number.data
        # phone_number = request.POST.get('phone_number', '')
        bg_img = _create_background_image()
        barcode_img = _generate_barcode_image(serial_number)
    return render_template('create_coupon.html', form=form)

