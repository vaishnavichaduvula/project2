import qrcode


#name = input("enter your name:")
#age = input("enter age:")
#education = input("enter your education:")
#data = {'name':name,'age':age,'education':education}
data = 'https://github.com/chaduvulasaireddy/event.git'

qr = qrcode.QRCode(
     version=5,
     box_size=5,
     border=3,
)



qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color='green',black_color='white')
img.save('doc.png')
img.show()
