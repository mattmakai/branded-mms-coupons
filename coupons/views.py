from flask import request, render_template, jsonify

from . import app
from .utils import _create_background_image, _generate_barcode_image

@app.route('/create/', methods=['GET', 'POST'])
def create_image():
    if request.method == 'POST':
        logo_file = request.files['file']
        try:
            img = Image.open(logo_file)
        except:
            # cannot open image
            render_template('invalid_file.html')
        serial_number = request.POST.get('serial_number', '')
        phone_number = request.POST.get('phone_number', '')
        # TODO: ensure barcode serial is numeric
        
        bg_img = _create_background_image()
        barcode_img = _generate_barcode_image(serial_number)
    else:
        render_template('upload_image.html')


