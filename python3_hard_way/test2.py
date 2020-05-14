from PIL import Image
import qrcode
image = qrcode.make("google.com")
image.show()
