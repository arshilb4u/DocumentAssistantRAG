
import qrcode
import os

os.makedirs('qr_codes', exist_ok=True)
url = 'www.udemy.com/course/langchain'

for i in range(1, 16):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f'qr_codes/udemy_qr_{i}.png')
