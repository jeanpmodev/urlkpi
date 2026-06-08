import os
import pycodestyle
import time
error_amout = 0
list_error_files = ""
file_amout = 0

print(2*"\n")
for dirpath, dirnames, filenames in os.walk("."):
    for filename in filenames:
        if filename.endswith(".py"):
            fchecker = pycodestyle.Checker(
                dirpath+"/"+filename, show_source=False)
            file_errors = fchecker.check_all()
            error_amout += file_errors
            if file_errors != 0:
                file_amout += 1
                list_error_files += filename+"\n"
                print(f"Found {file_errors} errors in "+filename)
                print(100*"  ")
                # print(filename + "                      ")
                # time.sleep(1)
print(1*"\n")
print("Total files with erros :"+str(file_amout))
time.sleep(1)
print(list_error_files)
time.sleep(1)
print("Total Errors " + str(error_amout))

# refatorar funcoes de erros e impressaão
# mandar pra view a lista de erros e quantitativos
