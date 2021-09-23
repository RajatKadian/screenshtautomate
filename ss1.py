import smtplib
from email.message import EmailMessage
import imghdr
import os
from selenium import webdriver
from PIL import Image
driver = webdriver.Chrome()

url = "https://www.geeksforgeeks.org/"
driver.get(url)

driver.save_screenshot("image.png")
image1 = Image.open("image.png")

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')


msg = EmailMessage()
msg['Subject'] = 'hello'
msg['From'] = EMAIL_ADDRESS
msg['to'] = 'rajat.kadian007@yahoo.com'
msg.set_content('HI')

with open('image.png','rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name

msg.add_attachment(file_data, maintype = 'image', subtype = file_type, filename = file_name)

with smtplib.SMTP('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)


    smtp.send_message(msg)


driver.get("https://<username>:<password>@www.example.com/index.html")