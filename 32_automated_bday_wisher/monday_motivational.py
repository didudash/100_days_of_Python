import smtplib
from dotenv import load_dotenv
import os
import datetime as dt
import random


def send_email(subject: str, chosen_quote: str) -> None:

    # Load environment variables
    load_dotenv()
    my_email = os.getenv("TEST_EMAIL")
    my_password = os.getenv("TEST_PASSWORD")
    recipient_email = os.getenv("RECIPIENT_EMAIL")

    try:
        connection = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient_email,
            msg=f"Subject:{subject}\n\n{chosen_quote}",
        )
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        connection.quit()


def choose_quote(quotes_file_path: str) -> str:
    with open(quotes_file_path) as file:
        quotes = file.readlines()
    chosen_quote = random.choice(quotes)
    return chosen_quote


if __name__ == "__main__":
    now = dt.datetime.now()
    day_of_week = now.weekday()
    print(day_of_week)
    if day_of_week == 0:
        chosen_quote = choose_quote("quotes.txt")
        send_email("Monday Quote", chosen_quote)
