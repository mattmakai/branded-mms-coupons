import barcode
import requests
from barcode.writer import ImageWriter
from PIL import Image
from StringIO import StringIO
from twilio.rest import TwilioRestClient

from config import TWILIO_NUMBER

client = TwilioRestClient()

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
    return barcode.get('ean13', serial_number, writer=ImageWriter())


def _combine_images_into_coupon(background_img, logo_img, barcode_img):
    pass


def _send_coupon_via_mms(finished_coupon, recipient_number, 
    msg_text="Scan me!"):
    to_number = "+1" + recipient_number
    client.messages.create(to=to_number, from_=TWILIO_NUMBER, 
    body=msg_text, 
    media_url="http://www.twilio.com/packages/company/img/logos_downloadable_logobrand.png")
