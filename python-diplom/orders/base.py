import os
import sys
import psycopg2
from dotenv import load_dotenv
load_dotenv()


def bases():
    conn = psycopg2.connect(dbname="postgres", user=os.getenv('POSTGRES_USER'),
                            password=os.getenv('POSTGRES_PASSWORD'), host=os.getenv('POSTGRES_HOST'))
    cursor = conn.cursor()
    conn.autocommit = True
    row = cursor

    if row:
        #sql = f"DROP DATABASE {os.getenv('POSTGRES_DB')}"
        print (f"База данных {os.getenv('POSTGRES_DB')} существует")
       # cursor.execute(sql)
        sys.exit(0)
    else:
        sql = f"CREATE DATABASE {os.getenv('POSTGRES_DB')}"
        cursor.execute(sql)
        print("База данных успешно создана")
    # #sql = f"DROP DATABASE {os.getenv('POSTGRES_DB')}"
    # # команда для создания базы данных
    # sql = f"CREATE DATABASE {os.getenv('POSTGRES_DB')}"
    #
    # # выполняем код sql
    # cursor.execute(sql)
    # print("База данных успешно создана")

    cursor.close()
    conn.close()
bases()
