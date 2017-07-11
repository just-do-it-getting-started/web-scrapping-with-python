import smtplib
from email.mime.text import MIMEText

msg = MIMEText("the body of the email is here")

msg["Subject"] = "An Email Alert"
msg["From"] = "kimshine@naver.com"
msg["To"] = "kimshinelove@gmail.com"

s = smtplib.SMTP("smtp.naver.com", 587)
s.ehlo()
s.starttls()
s.ehlo()
s.login("kimshine", "password")

s.send_message(msg)
s.quit()