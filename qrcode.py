import qrcode as qr
img= qr.make("https://www.youtube.com/watch?v=VAdGW7QDJiU&ab_channel=T-Series")
img.save("tseries.png")