import smtplib
import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
URL = "https://appbrewery.github.io/instant_pot/"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
price = soup.find(name = "span", class_="aok-offscreen")
price_as_float = float(price.text.replace("$", ""))
title = soup.find(id="productTitle").get_text().strip()
print(title)

target = 100
if target > price_as_float:
    message = f"{title} is on sale for {price}"
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=f"Subject:Amazon price alert!!\n\n{message}\n{URL}".encode("utf-8"))

