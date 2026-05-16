from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36"
}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

all_movies = soup.find_all(name="h3",class_="title")
movie_title = [movie.text for movie in all_movies ]
movies = movie_title[::-1]

with open("movie_title.txt", "w") as f:
    for movie in movies:
        f.write(f"{movies}\n")
