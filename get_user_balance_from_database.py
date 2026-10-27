import os
import sqlite3
from contextlib import closing
from pathlib import Path
from dotenv import load_dotenv

def get_user_balance_from_database(logged_in_user_name):

    load_dotenv()
    DATABASE_PATH = os.getenv("DATABASE_PATH")
    DATABASE_PATH = Path(DATABASE_PATH).expanduser()

    balance = 0

    try:
        with closing(sqlite3.connect(DATABASE_PATH)) as conn:
            with closing(conn.cursor()) as cursor:

                cursor.execute("select balance from users where user_name = ?", (logged_in_user_name))
                row = cursor.fetchone()
                balance = row[0]

        conn.commit()

    except sqlite3.Error as e:
        print(f"SQLite Error: {e}")

    return balance