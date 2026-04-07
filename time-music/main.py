import requests
from bs4 import BeautifulSoup
date_user = input("which year do you want to travel to? Type the date in this format YYYY-MM-DD")
URL = f"https://www.billboard.com/charts/hot-100/{date_user}/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36"
}
response = requests.get(url=URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
song_names_spans = soup.select("li ul li h3")
title = [song.text.strip() for song in song_names_spans]
print(title)