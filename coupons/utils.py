import barcode
from barcode.writer import ImageWriter
from PIL import Image

def _create_background_image(width=640, height=480, rgb=(255, 255, 255)):
    return Image.new('RGB', (width, height), rgb)


def _generate_barcode_image(serial_number='1234567890'):
    return barcode.get('ean13', serial_number, writer=ImageWriter())            
