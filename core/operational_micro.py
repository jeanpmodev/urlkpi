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
import os
import pycodestyle


def check_pep8():
    error_amount = 0
    list_error_files = ""
    file_amout = 0
    result = []
    error_spec = []

    return_dict_pep = {'error_amount': 0, 'list_error_files': '',
                       'file_amout': 0, 'result': [], 'error_spec': []}

    print(2*"\n")
    for dirpath, dirnames, filenames in os.walk("."):
        for filename in filenames:
            if filename.endswith(".py"):
                fchecker = pycodestyle.Checker(
                    dirpath+"/"+filename, show_source=False)
                file_errors = fchecker.check_all()
                error_amount += file_errors
                if file_errors != 0:
                    file_amout += 1
                    list_error_files += filename+"\n"
                    # print(f"Found {file_errors} errors in "+filename)
                    #print(100*"  ")
    result = list_error_files.split()
    for item in result:
        item = script_dir = os.path.dirname(os.path.realpath(__file__))
        error_spec = subprocess.run(
            ["pycodestyle", item],
            capture_output=True,  # Captures stdout and stderr
            text=True,            # Returns string instead of bytes
            encoding='utf-8'      # Ensures correct decoding
        )
        error_spec = error_spec.stdout
        error_spec = error_spec.replace(item, "")
        error_spec = error_spec.split('\n')

    print(1*"\n")
    print("Total files with erros :"+str(file_amout))
    time.sleep(1)
    # print(list_error_files)
    time.sleep(1)
    print("Total Errors " + str(error_amount))
    return_dict_pep["error_amount"] = error_amount
    return_dict_pep["list_error_files"] = list_error_files
    return_dict_pep["file_amout"] = file_amout
    return_dict_pep["result"] = result
    return_dict_pep["error_spec"] = error_spec
    return return_dict_pep


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
    git_log = generate_cmd_sub(
        '''git log --since='2026-05-01' --until='2026-05-31' --oneline''')
