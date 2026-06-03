#!/usr/bin/env python

# DATABASE OPERATIONAL


import sqlite3
from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "db.sqlite3"

# connect to db checker


def check_database_connection():
    print(str(DB_PATH))
    try:
        connection = sqlite3.connect(str(DB_PATH))
        cursor = connection.cursor()

        cursor.execute("SELECT 1;")
        cursor.fetchone()
        print("SQLite connection successful!")

        cursor.close()
        connection.close()
        return True

    except Exception as e:
        print(f"SQLite connection failed: {e}")
        return False


# show all tables in db
def show_tables():
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in cursor.fetchall()]
    print("\n")
    for item in tables:
        print(item)
    conn.close()
