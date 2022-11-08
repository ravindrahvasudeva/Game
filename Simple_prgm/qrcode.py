<<<<<<< HEAD
# Importing library
import qrcode
 
# Data to encode
data = "https://github.com/ravindrahvasudeva/Description/blob/master/index.html"
 
# Creating an instance of QRCode class
qr = qrcode.QRCode(version = 1,
                   box_size = 10,
                   border = 5)
 
# Adding data to the instance 'qr'
qr.add_data(data)
 
qr.make(fit = True)
img = qr.make_image(fill_color = 'Black',
                    back_color = 'white')
 
=======
# Importing library
import qrcode
 
# Data to encode
data = "https://github.com/ravindrahvasudeva/Description/blob/master/index.html"
 
# Creating an instance of QRCode class
qr = qrcode.QRCode(version = 1,
                   box_size = 10,
                   border = 5)
 
# Adding data to the instance 'qr'
qr.add_data(data)
 
qr.make(fit = True)
img = qr.make_image(fill_color = 'Black',
                    back_color = 'white')
 
>>>>>>> a15de333f5cb5d803fb18660f02ece1595789616
img.save('med.png')