import smtplib
import datetime as dt
import random

MY_EMAIL = 'kishrgdesai@gmail.com'
MY_PASSWORD = 'cwyk qsnk uwsj mprh'
now  = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,to_addrs=MY_EMAIL,msg=f"Subject:Monday motivation\n\n{quote}")
