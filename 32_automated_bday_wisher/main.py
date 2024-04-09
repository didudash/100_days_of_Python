import smtplib
from dotenv import load_dotenv
import os
import datetime as dt
import pandas as pd
import random
from typing import Optional, Tuple


def send_email(subject: str, email_text: str, email: str) -> None:

    # Load environment variables
    load_dotenv()
    my_email = os.getenv("TEST_EMAIL")
    my_password = os.getenv("TEST_PASSWORD")

    try:
        connection = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=f"Subject:{subject}\n\n{email_text}",
        )
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        connection.quit()


def find_matching_bday(
    bdays_file: str, month_now: int, day_now: int
) -> Optional[Tuple[str, str]]:
    data = pd.read_csv(bdays_file)

    filtered_data = data[(data["month"] == month_now) & (data["day"] == day_now)]

    # Assuming only one birthday per day, get the name and email if present
    if not filtered_data.empty:
        birthday_name = filtered_data["name"].iloc[0]
        birthday_email = filtered_data["email"].iloc[0]
        return birthday_name, birthday_email
    else:
        return None


def choose_random_letter(letters_path: str) -> str:
    try:
        letters_in_directory = os.listdir(letters_path)
        if letters_in_directory:
            return os.path.join(letters_path, random.choice(letters_in_directory))
        else:
            return None
    except FileNotFoundError:
        print("Directory does not exist.")
        return None


def personalize_letter(letter_file_path: str, name: str) -> str:
    try:
        with open(letter_file_path, "r", encoding="utf-8") as file:
            letter_contents = file.read()
            personalized_letter = letter_contents.replace("[NAME]", name)
        return personalized_letter
    except FileNotFoundError:
        print("The file was not found.")
        return ""


if __name__ == "__main__":
    now = dt.datetime.now()
    day_now = now.day
    month_now = now.month
    matching_bday = find_matching_bday("birthdays.csv", month_now, day_now)
    if matching_bday is not None:
        name, email = matching_bday
        letter_file_path = choose_random_letter("letter_templates")
        personalized_letter = personalize_letter(letter_file_path, name)
        send_email("It's your B-day!", personalized_letter, email)
    else:
        print("No bday today :(")
