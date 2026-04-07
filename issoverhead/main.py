import time

import requests
from datetime import datetime
from geopy.distance import geodesic
import smtplib

MY_LAT = 15.241686
MY_LONG = 74.112251




def position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    point1=[iss_latitude,iss_longitude]
    point2=[MY_LAT,MY_LONG]
    distance_km = geodesic(point1, point2).km
    if distance_km <= 5:
        return True
    else:
        return False


while True:
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hours = time_now.hour




    if position():
        if hours >= sunset or hours <= sunrise:
            with smtplib.SMTP('smtp.gmail.com', 587) as connection:
                connection.starttls()
                connection.login("kishrgdesai@gmail.com", "cwyk qsnk uwsj mprh")
                connection.sendmail(to_addrs="kishrgdesai@gmail.com",from_addr="kishrgdesai@gmail.com",msg="Subject: iss location \n\n  look up into the sky")
    time.sleep(60)



