import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
#from selenium import webdriver
from PIL import Image
#driver = webdriver.Chrome()
#url = "https://stage-app.photo-wonder.com"
#driver.get(url)
#driver.save_screenshot("image.png")
#image1 = Image.open("image.png")
me = "rajat@photo-wonder.com"
my_password ="byut ykio houd euck"
you = "joginder@photo-wonder.com"
msg = MIMEMultipart('alternative')
msg['Subject'] = "Important KPI'S"
msg['From'] = me
msg['To'] = you
html = '<html><body><div style ="height:600px;width:300px;text-align:center;font-size:18pt;color:black;background-color:"grey"><p style ="width:300px;text-align:center;font-size:18pt;color:red;">Important KPI </p><a href="https://stage-app.photo-wonder.com/admin/dashboard"><button style="width:300px;font-size:13pt;padding:2px; border:3px solid green">view order KPI</button></a> </div></body></html>'
part2 = MIMEText(html, 'html')
msg.attach(part2)
#  fp = open('image.png','rb')
#msgImage = MIMEImage(fp.read())
#fp.close()
#msgImage.add_header('Content-ID', '<image1>')
#msg.attach(msgImage)
s = smtplib.SMTP_SSL('smtp.gmail.com')
s.login(me, my_password)
s.sendmail(me, you, msg.as_string())
s.quit()