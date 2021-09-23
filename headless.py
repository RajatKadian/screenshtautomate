from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from selenium import webdriver
import smtplib

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)" \
             " Chrome/90.0.4430.85 Safari/537.36"
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
driver.get("https://stage-app.photo-wonder.com/admin/orders")
driver.get_screenshot_as_file("ss.png")
print(driver.title)

me = "rajat@photo-wonder.com"
my_password = "byut ykio houd euck"
you = "rajat.kadian007@yahoo.com"

msg = MIMEMultipart('alternative')
msg['Subject'] = "Alert"
msg['From'] = me
msg['To'] = you

html = '<html><body><p>Reports order</p><img src="cid:image"></body></html>'
part2 = MIMEText(html, 'html')

msg.attach(part2)
fp = open('ss.png','rb')
msgImage = MIMEImage(fp.read())
fp.close()


msgImage.add_header('Content-ID', '<image1>')


msg.attach(msgImage)



s = smtplib.SMTP_SSL('smtp.gmail.com')

s.login(me, my_password)

s.sendmail(me, you, msg.as_string())
s.quit()