import pandas
import datetime as dt
import random
import smtplib

MY_EMAIL = "<INSERT-EMAIL>"
PASSWORD = "<INSERT-PASSWORD>"

SMTP = "smtp.gmail.com"

# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")     # creates dataframe

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()     # gets current date
month = now.month   # gets current month from date
day = now.day   # gets current day from date

try:    #tries to find a row where todays day and month matches someones birthday
    row = data.loc[(data["day"] == day) & (data["month"] == month)]     # gets a row where day and month match current day and month
    name = row["name"].values[0]  # gets a name from chosen row (we have an array and access the first and only value by values[0]
    email = row["email"].values[0]  # gets an email address from chosen row
except IndexError:  # in case of no match, nobody has birthday today
    print("It's nobody's birthday today.")

else:
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    random_num = random.randint(1, 3)   # to pick a different letter template
    new_letter = f"letter_for_{name}.txt"   #name of new letter
    with open(f"./letter_templates/letter_{random_num}.txt", mode="r") as starting_letter:  # opens template letter
        with open(new_letter, mode="w") as letter:  # creates new letter for someone
            for line in starting_letter:    # copies every line from template
                letter.write(line.replace("[NAME]", name))  # replaces word name with an actual name

    with open(new_letter, mode="r") as file:    # opens new letter for someone
        content = file.read()   # gets its content

# 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP(SMTP) as connection:  # sets up mail sending process
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=email,
            msg=f"Subject:Happy birthday\n\n{content}"  # sends content as message
        )



