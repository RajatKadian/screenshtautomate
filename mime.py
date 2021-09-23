import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from selenium import webdriver
from PIL import Image
driver = webdriver.Chrome()

#https://<username>:<password>@
#driver.get("https://<username>:<password>@www.example.com/index.html")
url = "https://stage-app.photo-wonder.com/admin/user-profile"
driver.get(url)
#driver.execute_script('browserstack_executor: {\"action\": \"dismissBasicAuth\",\"arguments\": {\"timeout\": \"<time in milliseconds>\"}}')


driver.save_screenshot("image.png")
image1 = Image.open("image.png")

me = "rajat@photo-wonder.com"
my_password = "byut ykio houd euck"
you = "rajat.kadian007@yahoo.com"

msg = MIMEMultipart('alternative')
msg['Subject'] = "Alert"
msg['From'] = me
msg['To'] = you

html = '<html><body><p>Reports order</p><img src="cid:image1"></body></html>'
part2 = MIMEText(html, 'html')

msg.attach(part2)
fp = open('image1.png','rb')
msgImage = MIMEImage(fp.read())
fp.close()

msgImage.add_header('Content-ID', '<image1>')

msg.attach(msgImage)


s = smtplib.SMTP_SSL('smtp.gmail.com')

s.login(me, my_password)

s.sendmail(me, you, msg.as_string())
s.quit()