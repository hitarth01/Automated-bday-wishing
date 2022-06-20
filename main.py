import smtplib
import datetime as dt
import pandas
import random
import config

now = dt.datetime.now()
current_day = now.day
current_month = now.month
month_day = (current_month, current_day)

birthdays = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day):data_row for (index, data_row) in birthdays.iterrows()}


if month_day  in birthdays_dict:
    birthday_person = birthdays_dict[month_day]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter:
        content = letter.read()
        content =   content.replace("[NAME]", birthday_person["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=config.my_email, password=config.password)
        connection.sendmail(from_addr=config.my_email, to_addrs=birthday_person["email"], msg=f"Subject:Happy Birthday\n\n{content}")

    

