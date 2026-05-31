#!/usr/bin/env python

# basic but useful functions

# sample sorted a list 
# from operational import sorted_list
# from manager import modules_requests
# sorted_list(modules_requests)
import time
import sqlite3
from pathlib import Path
import subprocess

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "db.sqlite3"


def sorted_list(unordered_list):
	for item in unordered_list:
		print(item)
		time.sleep(0.2)
	ordered_list = sorted(unordered_list)
	for item in ordered_list:
		print(item)
		time.sleep(0.2)
	return ordered_list

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

