import requests
from dotenv import load_dotenv
import os
from datetime import datetime
import smtplib
import time

"""
requests response codes: 
1XX: Informational
2XX: Success 
3XX: Redirection
4XX: Client Error  
5XX: Server Error 
"""


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


def get_iss_position() -> dict:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_position = {"lat": iss_latitude, "lng": iss_longitude}
    return iss_position


def is_position_close_and_dark(iss_position: dict) -> bool:

    load_dotenv()
    lat = float(os.getenv("LATITUDE"))
    lng = float(os.getenv("LONGITUDE"))
    parameters = {"lat": lat, "lng": lng, "formatted": 0}
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[-1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[-1].split(":")[0])
    time_now = datetime.now().hour
    is_target_location = (
        iss_position["lat"] - 5 <= lat <= iss_position["lat"] + 5
    ) and (iss_position["lng"] - 5 <= lng <= iss_position["lng"] + 5)
    is_dark = time_now >= sunset or time_now <= sunrise

    if is_target_location and is_dark:
        return True
    else:
        return False


if __name__ == "__main__":
    while True:
        iss_position = get_iss_position()
        if is_position_close_and_dark(iss_position):
            load_dotenv()
            recipient_email = os.getenv("RECIPIENT_EMAIL")
            send_email(
                subject="Look UP!",
                email_text="Look up the ISS is on the sky",
                email=recipient_email,
            )
        time.sleep(60)
