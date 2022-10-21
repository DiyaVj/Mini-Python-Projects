#pip install qrcode
import qrcode
#place your url inside single quotes
url = 'https://hacktoberfest.com/'
img=qrcode.make(url)
img.save('myqrcode.png')
img.show()
