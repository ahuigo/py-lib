#For QR code image creation:

import pyqrcode

def createQR(txt="test"):
	qr = pyqrcode.create(txt)
	file = "test1.png"
	qr.png(file, scale=6)
	return file

def parseQR(file):
	from PIL import Image
	from pyzbar.pyzbar import decode
	data = decode(Image.open('test1.png'))
	print(data)
	return data


if __name__ == "__main__":
	file = createQR("test1")
	parseQR(file)
