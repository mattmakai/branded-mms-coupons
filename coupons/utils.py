import barcode
import requests
import uuid
from barcode.writer import ImageWriter
from PIL import Image
from StringIO import StringIO
from twilio.rest import TwilioRestClient

from config import TWILIO_NUMBER, COUPON_SAVE_DIR, QUALIFIED_MEDIA_URL

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
    bg_width = logo_img.size[0] + barcode_img.size[0] + extra_spacing
    if logo_img.size[1] > barcode_img.size[1]:
        bg_height = logo_img.size[1] + extra_spacing
    else:
        bg_height = barcode_img.size[1] + extra_spacing
    bg_img = _create_background_image(bg_width, bg_height)
    logo_offset = (extra_spacing / 2, extra_spacing / 2)
    try:
        bg_img.paste(logo_img, logo_offset, logo_img)
    except:
        # try with the mask
        bg_img.paste(logo_img, logo_offset)

    barcode_offset = (logo_img.size[0] + \
                      extra_spacing / 3, extra_spacing / 2)
    bg_img.paste(barcode_img, barcode_offset)
    return _save_image(bg_img)


def _save_image(image):
    unique_filename = str(uuid.uuid4()) + '.png'
    image.save(COUPON_SAVE_DIR + unique_filename)
    return unique_filename

def _send_coupon_via_mms(coupon_filename, recipient_number, 
                         msg_text="Scan me for 20% off!"):
    to_number = "+1" + recipient_number
    media_url = QUALIFIED_MEDIA_URL + coupon_filename
    client.messages.create(to=to_number, from_=TWILIO_NUMBER, 
        body=msg_text, media_url=media_url)
