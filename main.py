import smtplib
import random
import datetime
import pandas

# - Extra Hard Starting Project -#

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the people's actual
# name from birthdays.csv

# 4. Send the letter generated in step 3 to that people's email address.

email = "adisenpai101@gmail.com"
password = "ar_@12345"
receiver_mail = "adi.adityaraj24@gmail.com"

peoples_df = pandas.read_csv('birthdays.csv')
date_list = peoples_df['day'].tolist()
month_list = peoples_df['month'].tolist()

today = datetime.datetime.now()
today_month = today.month
today_date = today.day

if today_month in month_list:
    if today_date in date_list:
        people = peoples_df[peoples_df['month'] == today_month]
        people = people[people['day'] == today_date]
        bd_peoples = people.to_dict(orient="records")

num = random.randint(1, 3)

with open(f'letter_templates/letter_{num}.txt', 'r') as file_data:
    letter_templates = file_data.read()

with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
    connection.starttls()
    connection.login(user=email, password=password)

    try:
        for person in bd_peoples:
            letter_templates = letter_templates.replace("[NAME]", f'{person["name"]}')
            connection.sendmail(
                from_addr=email,
                to_addrs=f'{person["email"]}',
                msg=f'Subject:Happy Birthday\n\n{letter_templates}'
            )
            print(f"Send the birthday wish to: {person['name']}")
    except NameError:
        print('No ones birthday today!')

print("All done")

