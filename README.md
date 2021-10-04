# Birthday Bot
Sends one of three template emails to a person on their birthday. People are defined in a database file.

## How to use
These parameters need to be set:
```python
SMTP = "smtp.gmail.com"
MY_EMAIL = "<INSERT-EMAIL>"
PASSWORD = "<INSERT-PASSWORD>"
```

People in the database are saved in a following format
```csv
NAME,EMAIL,YEAR,MONTH,DAY
Jane Doe,example@domain.com,1961,5,9
```

Letters are saved in letter_templates folder
```
letter_1.txt
letter_2.txt
letter_3.txt
```