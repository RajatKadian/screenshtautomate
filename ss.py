# from selenium import webdriver
# from PIL import Image
# driver = webdriver.Chrome()
# import email_to
# url = "https://www.geeksforgeeks.org/"
# driver.get(url)
# driver.save_screenshot("image1.png")
# image1 = Image.open("image1.png")
# message = email_to.Message('# Reports Daily')
# message.style = 'h1 { color:green }'
# server = email_to.EmailServer('smtp.gmail.com', 587, 'rajat@photo-wonder.com', 'byut ykio houd euck')
# server.send_message(message, 'rajat.kadian007@yahoo.com', 'Things are awesome')

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from selenium import webdriver
from PIL import Image
driver = webdriver.Chrome()

url = "https://stage-app.photo-wonder.com/orderKPI/order-received"
driver.get(url)
driver.save_screenshot("image1.png")
image1 = Image.open("image1.png")

url = "https://app.slack.com/client/T017ZJN5LD9/D01Q63ZAQ8Z"
driver.get(url)
driver.save_screenshot("image2.png")
image = Image.open("image2.png")

me = "rajat@photo-wonder.com"
my_password = "byut ykio houd euck"
you = "rajat.kadian007@yahoo.com"

msg = MIMEMultipart('alternative')
msg['Subject'] = "Alert"
msg['From'] = me
msg['To'] = you

html = '<html><body><p>Reports order</p><img src="cid:image"><img src = "cid1:image"></body></html>'
part2 = MIMEText(html, 'html')

msg.attach(part2)
fp = open('image1.png','rb')
msgImage = MIMEImage(fp.read())
fp.close()

fp = open('image2.png','rb')
msgImage2 = MIMEImage(fp.read())
fp.close()

msgImage.add_header('Content-ID', '<image1>')
msgImage2.add_header('Content-ID1', '<image2>')

msg.attach(msgImage)
msg.attach(msgImage2)


s = smtplib.SMTP_SSL('smtp.gmail.com')

s.login(me, my_password)

s.sendmail(me, you, msg.as_string())
s.quit()
