import barcode
import requests
from barcode.writer import ImageWriter
from PIL import Image
from StringIO import StringIO


def _open_image_file_from_url(image_file_url):
    image_request = requests.get(image_file_url)
    if image_request.status_code == 200:
        return Image.open(StringIO(image_request.content))
    return False


def _create_background_image(width=640, height=480, rgb=(255, 255, 255)):
    return Image.new('RGB', (width, height), rgb)


def _generate_barcode_image(serial_number='1234567890'):
    return barcode.get('ean13', serial_number, writer=ImageWriter())            
