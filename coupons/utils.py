import barcode
import requests
import uuid
from barcode.writer import ImageWriter
from PIL import Image
from StringIO import StringIO
from twilio.rest import TwilioRestClient

from config import TWILIO_NUMBER, COUPON_SAVE_DIR

client = TwilioRestClient()
extra_spacing = 50

def _open_image_file_from_url(image_file_url):
    if not image_file_url:
        return False
    image_request = requests.get(image_file_url)
    if image_request.status_code == 200:
        return Image.open(StringIO(image_request.content))
    return False


def _create_background_image(width=640, height=480, rgb=(255, 255, 255)):
    return Image.new('RGB', (width, height), rgb)


def _generate_barcode_image(serial_number='1234567890'):
    return barcode.get('ean13', serial_number, writer=ImageWriter()).render()


def _combine_images_into_coupon(logo_img, barcode_img):
    if logo_img.size[0] > barcode_img.size[0]:
        bg_width = logo_img.size[0] + extra_spacing
    else:
        bg_width = barcode_img.size[0] + extra_spacing
    bg_height = logo_img.size[1] + barcode_img.size[1] + extra_spacing
    bg_img = _create_background_image(bg_width, bg_height)
    offset = (extra_spacing / 2, extra_spacing / 2)
    bg_img.paste(logo_img, offset)
    return _save_image(bg_img)


def _save_image(image):
    unique_filename_full_path = COUPON_SAVE_DIR + str(uuid.uuid4()) + '.png'
    image.save(unique_filename_full_path)
    return unique_filename_full_path

def _send_coupon_via_mms(finished_coupon_url, recipient_number, 
                         msg_text="Scan me!"):
    to_number = "+1" + recipient_number
    client.messages.create(to=to_number, from_=TWILIO_NUMBER, 
        body=msg_text, media_url=finished_coupon_url)
