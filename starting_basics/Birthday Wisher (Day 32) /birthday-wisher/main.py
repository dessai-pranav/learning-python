import smtplib

import pandas as pd
import datetime as dt
now = dt.datetime.now()
today = (now.month,now.day)
MY_EMAIL = 'kishrgdesai@gmail'
MY_PASSWORD = 'cwyk qsnk uwsj mprh'

data = pd.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"],data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path ="letter_templates/letter_1.txt"
    with open(file_path) as f:
        content = f.read()
        content = content.replace("[NAME]",birthday_person["name"])

        with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL,MY_PASSWORD)
            connection.sendmail(MY_EMAIL,birthday_person["email"],msg=f"Subject:Happy Birthday!\n\n{content}")






