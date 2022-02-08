import smtplib


BODY = "\r\n".join((
    "From: T-Centr@yandex.ru",
    # 'From: "Валерий" <T-Centr@yandex.ru>', можно и так
    "To: T-Centr@yandex.ru",
    "Subject: Тестовое письмо",
    "Content-Type: text/plain; charset=utf-8",
    "",
    "Привет! Это письмо из Python"
)).encode("UTF-8")

user = "T-Centr"
password = "XXXXX"
server = smtplib.SMTP_SSL("smtp.yandex.ru", 465)
server.login(user, password)
server.sendmail("T-Centr@yandex.ru", "T-Centr@yandex.ru", BODY)
server.quit()
