# from selenium import webdriver
# from PIL import Image
import smtplib
# from email.MIMEImage import MIMEImage
#
#
# driver = webdriver.Chrome()
#
#
# url = "https://stage-app.photo-wonder.com/admin/dashboard"
#
#
# driver.get(url)
#
# driver.save_screenshot("image.png")
#
#
# image = Image.open("image.png")
#
#

#
# server = smtplib.SMTP_SSL("smtp.gmail.com",465)
# server.login("rajat@photo-wonder.com", "byut ykio houd euck")
# server.sendmail("rajat@photo-wonder.com", "rajat.kadian007@yahoo.com", msgRoot.as_string())
# fp.close()
#
# server.quit()
#
#
#
#

# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# #import smtplib
#
# message = MIMEMultipart('alternative')
# message['Subject'] = 'Test'
# message['From'] = 'rajat@photo-wonder.com'
# message['To'] = 'rajat.kadian007@yahoo.com'
#
# message.attach(MIMEText('# A Heading\nSomething else in the body', 'plain')
# message.attach(MIMEText('<h1 style="color: blue">A Heading</a><p>Something else in the body</p>', 'html')
#
# server = smtplib.SMTP('smtp.gmail.com', 465)
# server.starttls()
# server.login('rajat@photo-wonder.com', 'byut ykio houd euck')
# server.sendmail('rajat@photo-wonder.com', 'rajat.kadian007@yahoo.com', message.as_string())
# server.quit()

import email_to

message = email_to.Message('# Every thing is ok')
message.add('Everything has been running fine for days.')
message.add('Probably time to build something new and break everything')
message.style = 'h1 { color: green }'

server = email_to.EmailServer('smtp.gmail.com', 587, 'rajat@photo-wonder.com', 'byut ykio houd euck')
server.send_message(message, 'rajat.kadian007@yahoo.com', 'Things are awesome')
