import os
import sqlite3
from pathlib import Path
from contextlib import closing
from dotenv import load_dotenv

def update_user_balance_in_database(user_name, updated_balance):

    load_dotenv()

    DATABASE_PATH = os.getenv("DATABASE_PATH")
    DATABASE_PATH = Path(DATABASE_PATH).expanduser()

    try:
        with closing(sqlite3.connect(DATABASE_PATH)) as conn:
            with closing(conn.cursor()) as cursor:

                cursor.execute("update users set balance = ? where user_name = ?", (user_name, updated_balance))

                conn.commit()

    except sqlite3.Error as e:
        print(f"SQLite Error: {e}")