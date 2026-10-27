import os
import sqlite3
from contextlib import closing
from pathlib import Path
from dotenv import load_dotenv

def get_present_user_names():

    load_dotenv()

    rows_list = []

    DATABASE_PATH = os.getenv("DATABASE_PATH")
    DATABASE_PATH = Path(DATABASE_PATH).expanduser()
    
    try:
        with closing(sqlite3.connect(DATABASE_PATH)) as conn:
            with closing(conn.cursor()) as cursor:

                cursor.execute("select user_name from users")
                rows_list.append(cursor.fetchall())

                conn.commit()

    except sqlite3.Error as e:
        print(f"SQLite Error: {e}")


    present_user_names_list = []
    for rows in rows_list:
        present_user_names_list.append(rows[0])

    return present_user_names_list