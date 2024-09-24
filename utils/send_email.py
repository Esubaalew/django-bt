import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from os import getenv


def send_email(to_email, subject, body):
    smtp_server = getenv('SMTP_SERVER')
    smtp_port = getenv('SMTP_PORT')
    smtp_user = getenv('SMTP_USER')
    smtp_password = getenv('SMTP_PASSWORD')

    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(smtp_user, to_email, msg.as_string())
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")
