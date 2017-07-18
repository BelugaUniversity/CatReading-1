# **coding: utf-8**
# from django.test import TestCase
# Create your tests here.
import qrcode

import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('http://192.168.1.118/static/1.pdf')
qr.make(fit=True)
img = qr.make_image()
img.save('123.png')