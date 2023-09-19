import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(message, topic):
    smtp_server = "smtp.gmail.com"
    port = 587
    password = "liaq grpx ysjo endi "
    sender_email = "oyakovenko.it@gmail.com"
    receiver_email = "oyakovenko.it@gmail.com"
    subject = "Email from portfolio web site"
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg['Topic'] = topic
    msg.attach(MIMEText(message, 'plain'))
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())


