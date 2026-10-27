import os
import sqlite3
from contextlib import closing
from pathlib import Path
from dotenv import load_dotenv

def create_database():
    load_dotenv(override=True)
    DATABASE_PATH = os.getenv("DATABASE_PATH")
    DATABASE_PATH = Path(DATABASE_PATH).expanduser()
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)

    try:
        with closing(sqlite3.connect(DATABASE_PATH)) as conn:
            with closing(conn.cursor()) as cursor:

                cursor.execute("""
                    create table if not exists users(
                        user_id integer primary key autoincrement,
                        user_name text not null unique,
                        full_name text not null, 
                        balance real not null default 0.00,
                        pin_hash text not null
                    )
                """)

                cursor.execute("""
                    insert or ignore into sqlite_sequence (name, seq) values ('users', 999)
                """)
                
            conn.commit()

    except sqlite3.Error as e:
        print(f"SQLite Error Occured: {e}")