#!/usr/bin/env python

# BASIC BUT USEFUL FUNCTIONS

# sample sorted a list
# from operational import sorted_list
# from manager import modules_requests
# sorted_list(modules_requests)
import time
import sqlite3
from pathlib import Path
import subprocess

# generate ordered list


def sorted_list(unordered_list):
    for item in unordered_list:
        print(item)
        time.sleep(0.2)
    ordered_list = sorted(unordered_list)
    for item in ordered_list:
        print(item)
        time.sleep(0.2)
    return ordered_list

# generate subprocess command from text


def generate_cmd_sub(subprocess_list):
    subprocess_list = subprocess_list.split()
    result = subprocess.run(subprocess_list)
    return result

# generate uml


def generate_uml():
    generate_cmd_sub("python3 manage.py graph_models -a -g --dot -o uml2.dot")
    generate_cmd_sub("dot -Tpng uml2.dot -ouml2.png")


# generate git log


def generate_git_log():
    git_log = generate_cmd_sub('''git log --since='2026-05-01' --until='2026-05-31' --oneline''' )




