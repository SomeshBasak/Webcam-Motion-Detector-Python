import smtplib, ssl
import imghdr
from email.message import EmailMessage

PASSWORD = ""   # Enter your password inside quotes
SENDER = ""     # Enter your email address inside quotes
RECEIVER = ""     # Enter receiver email address inside quotes


def send_email(image_path):
    print("send_email func started")
    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up!"
    email_message.set_content("Hey, We just showed a new customer!")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()
    print("send_email func ended")


if __name__ == "__main__":
    send_email(image_path="images/9.png")