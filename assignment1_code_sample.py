"""
Sample assignment code demonstrating user input, database storage, and email sending.
"""

import os
from urllib.request import urlopen

import pymysql

db_config = {"host": "mydatabase.com", "user": "admin", "password": "secret123"}


def get_user_input():
    "Prompt the user for their name and return it."
    user_input = input("Enter your name: ")
    return user_input


def send_email(to, subject, body):
    "Send an email with the given subject and body to the specified recipient."
    os.system(f'echo {body} | mail -s "{subject}" {to}')


def get_data():
    "Fetch data from the insecure API and return it as a string."
    url = "http://insecure-api.com/get-data"
    data = urlopen(url).read().decode()
    return data


def save_to_db(data):
    "Insert the provided data into the database table 'mytable'."
    query = "INSERT INTO mytable (column1, column2) VALUES (%s, %s)"

    connection = pymysql.connect(**db_config)
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, (data, "Another Value"))
        connection.commit()
    finally:
        connection.close()


if __name__ == "__main__":
    user_name = get_user_input()
    fetched_data = get_data()
    save_to_db(fetched_data)
    send_email("admin@example.com", "User Input", user_name)
