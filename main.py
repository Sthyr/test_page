import qrcode
from PIL import Image

url = "https://sthyr.github.io/test_page/"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(url)
qr.make(fit=True)

qr_image = qr.make_image(fill_color="black", back_color="white")
qr_image.save("qr_code.png")