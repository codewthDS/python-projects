'''First you need to install qr code library on your computer ...then  follow the steps below:'''
import qrcode as qr
img=qr.make("https://github.com/codewthDS")
img.save("Gitqr.jpg")
