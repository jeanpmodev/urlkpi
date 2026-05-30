#!/usr/bin/env python

# basic but useful functions

# sample sorted a list 
# from operational import sorted_list
# from manager import modules_requests
# sorted_list(modules_requests)
import time

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

