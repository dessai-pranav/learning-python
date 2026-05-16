import smtplib
import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
URL = "https://www.amazon.in/Ibanez-GRGR221PA-Electric-Guitar-Burst/dp/B08SHLHBGT/ref=sr_1_19?crid=2TJXJEXX1OMQE&dib=eyJ2IjoiMSJ9.4pXLz-ZdIfBcFPz_QCaWA2SPLU8kTZy9F3HzK8Q-CQtsjcAiqIk7utBok7IqSfSIaPDwwoVgEsZKLJla9opLECanIK47xizWCOVDtNaU0BiFJSj1xsSUk0VStu6TqducxQ4nogjf0gFabiTwQ5Apb3VJQPtRiR5MnTr0eYDBgMrH0-AmsDyRPkLvPbg-h5X4rqqf6VNNGN5m8iATGoOVBWKCRPu8lCOz6m8mFZDnoPxN1PwFiXva0PVXo3LsmXnJ0mSF92KzhE9wxVJa8ULNhXb4eO3sjKI1hMZMWv7yPYo.tivN0sOU2114rZw2Ecsdr0PmjJ2ep_Za1AvwUruiVrQ&dib_tag=se&keywords=ibanez+electric+guitar&nsdOptOutParam=true&qid=1775577850&sprefix=ibanez%2Caps%2C493&sr=8-19"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "en-IN,en;q=0.9"
}
response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
price = soup.find(name = "span", class_="a-price-whole")
price_as_float = float(price.text.replace(",", ""))
title = soup.find(id="productTitle").get_text().strip()
print(price_as_float)

target = 100
if target > price_as_float:
    message = f"{title} is on sale for {price}"
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=f"Subject:Amazon price alert!!\n\n{message}\n{URL}".encode("utf-8"))

