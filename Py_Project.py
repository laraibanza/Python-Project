import datetime  as dt
now=dt.datetime.now()
print(now)
year=now.year
print("The current year is :",year)
month=now.month
print("The current month is :",month)
day=now.weekday()
print("The current day is :",day)

Custom_=dt.datetime(year= 2001, month=3 , day=9, hour=1 , minute=30)
print(Custom_)





import smtplib
my_email="ellenkeller180@gmail.com"
password="pypr12345@"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(my_email,password)
    connection.sendmail(from_addr=my_email,
     to_addrs="my_email" , 
     msg="Subject:Python Project\n\nHello how r u?"
    )



import smtplib
import datetime as dt
import random
my_email="ellenkeller180@gmail.com"
password="pypr12345@"
now=dt.datetime.now()
weekday=now.weekday()
print(weekday)
if weekday==3:
    with open("quotes.txt", encoding = 'utf-8') as quote_file:
        all_quotes=quote_file.readlines()
        quote = random.choice(all_quotes)
        print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(from_addr=my_email,
        to_addrs=my_email , 
        msg=f"Subject: Monday Motivational Quote\n\n{quote}".encode('utf-8')
    )