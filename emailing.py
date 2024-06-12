import smtplib
import imghdr
from email.message import EmailMessage

PASSWORD = "wezb hrfb fapm pqau"
SENDER = "mjah.py@gmail.com"
RECEIVER = "mjah.py@gmail.com"

def send_email(image):
    email_message = EmailMessage()
    email_message["Subject"] = "Webcam App Email"
    email_message.set_content("Sending over a new webcam image!")

    # open image path, rb=binary file type
    with open(image, "rb") as file:
        content = file.read()
        # imghdr.what() will help us figure out what type of image (jpg, png)
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()

if __name__ == "__main__":
    send_email(image="images/153.png")