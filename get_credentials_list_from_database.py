import os
import sqlite3
from contextlib import closing
from pathlib import Path
from dotenv import load_dotenv

def get_credentials_list_from_database():

    load_dotenv()
    DATABASE_PATH = os.getenv("DATABASE_PATH")
    DATABASE_PATH = Path(DATABASE_PATH).expanduser()

    credentials_list = []
    
    try:
        with closing(sqlite3.connect(DATABASE_PATH)) as conn:
            with closing(conn.cursor()) as cursor:

                cursor.execute("select user_name, user_pin from users")
                credentials_list.append(cursor.fetchall())

        conn.commit()

    except sqlite3.Error as e:
        print(f"SQLite Error: {e}")

    return credentials_list