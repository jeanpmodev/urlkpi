#!/usr/bin/env python

# SERVICE OPERATIONAL 

import time
import sqlite3
from pathlib import Path
import subprocess

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "db.sqlite3"

def check_service_firewall():
    result = subprocess.run(
            ['sudo', 'ufw', 'status', 'verbose'],
            capture_output=True,
            text=True,
            check=True
        )
    return result.stdout

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

