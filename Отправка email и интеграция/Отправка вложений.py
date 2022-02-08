import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


letter = MIMEMultipart()
letter["From"] = "Валерий"
letter["Subject"] = "Активности в парках Москвы"
letter["Content-Type"] = "text/html; charset=utf-8"
letter["To"] = "support@ittensive.com"
letter.attach(
    MIMEText(open("parks.html", "r", encoding="UTF-8").read(), 'html')
)

attachement = MIMEBase('application', 'pdf')
attachement.set_payload(open('parks.pdf', 'rb').read())
attachement.add_header(
    'Content-Disposition', 'attachement; filename="parks.pdf"'
)

encoders.encode_base64(attachement)
letter.attach(attachement)
user = 'T-Centr'
password = "XXXX"
server = smtplib.SMTP_SSL("smtp.yandex.com", 465)
server.login(user, password)
server.sendmail("T-Centr@yandex.ru", "T-Centr@yandex.ru", letter.as_string())
server.quit()
