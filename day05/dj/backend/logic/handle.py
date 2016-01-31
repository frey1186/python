__author__ = 'felo'

from backend.db import sql_api


def home():
    print("welcome to home page...")
    q_data = sql_api.select("alex", "123")
    print(q_data)


def movie():
    print("welcome to movie page...")
def tv():
    print("welcome to tv page...")
