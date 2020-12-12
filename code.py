import os
import qrcode

link = input("Enter the link for QR code generation: ")
img = qrcode.make(link)
img.save("qr.png", "PNG")
os.system("open qr.png")
