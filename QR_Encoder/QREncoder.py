# Simple QR Encoder
import qrcode

# The variable to store the information
link = "https://https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Encoding The Link
image = qrcode.make(link)
print(type(image))

# Save the QR file
img.save("qr_test.jpg")
