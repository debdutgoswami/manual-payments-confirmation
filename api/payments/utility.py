import requests, json, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendemail(server, name: str, email: str):
    fromaddr = "youremail"
    toaddr = email
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "IMPORTANT: Confirmation of Payment"
    body = f"""Hi {name},

    You have successfully paid the amount. This is the confirmation mail for the payment. Keep this mail safe.

    Regards.
    """
    msg.attach(MIMEText(body))
    text = msg.as_string()

    return text