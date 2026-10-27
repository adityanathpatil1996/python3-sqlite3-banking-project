import os
import sqlite3
from pathlib import Path
from contextlib import closing
from dotenv import load_dotenv

def add_new_user_to_database(new_user):

    load_dotenv()

    DATABASE_PATH = os.getenv("DATABASE_PATH")
    DATABASE_PATH = Path(DATABASE_PATH).expanduser()

    try:
        with closing(sqlite3.connect(DATABASE_PATH)) as conn:
            with closing(conn.cursor()) as cursor:

                cursor.execute("insert into users (user_name, full_name, pin_hash) values (?, ?, ?)",
                               (new_user.user_name, new_user.full_name, new_user.pin))

                conn.commit()

    except sqlite3.Error as e:
        print(f"SQLite Error: {e}")

    print("Account Created")