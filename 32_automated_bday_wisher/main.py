import smtplib
from dotenv import load_dotenv
import os

# TODO: fix authentication error
# Load environment variables
load_dotenv()

# Get environment variables or prompt for input if not found
my_email = os.getenv("TEST_EMAIL") or input("Enter your email: ")
my_password = os.getenv("TEST_PASSWORD") or input("Enter your password: ")
recipient_email = os.getenv("RECIPIENT_EMAIL") or input("Enter recipient email: ")

# Setup connection and send email
try:
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=recipient_email,
        msg="Subject:Hello\n\nThis is the body of the email.",
    )
    print("Email sent successfully!")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    connection.close()
