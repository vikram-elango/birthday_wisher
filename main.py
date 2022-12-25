import pandas as pd
from smtplib import *
import datetime as dt
import random
PLACEHOLDER='[NAME]'


my_email="xyz@gmail.com"
password="xyz"

today=dt.datetime.now()

birth=pd.read_csv('birthdays.csv')

birth_name=birth.name.to_list()
birth_month=birth.month.to_list()
birth_day=birth.day.to_list()
birth_email=birth.email.to_list()





for i in range(0,len(birth_name)):
    if today.month==birth_month[i] and today.day==birth_day[i]:
        random_letter=random.randint(1,3)
        with open(f"letter_templates/letter_{random_letter}.txt") as letter:
            data_1=letter.read()
            data_updated=data_1.replace(PLACEHOLDER,birth_name[i])

            with SMTP("smtp.gmail.com",587) as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email,to_addrs=birth_email[i],
                                    msg=f"Subject: HAPPY BIRTHDAY!!!\n\n"
                                        f"{data_updated}")























