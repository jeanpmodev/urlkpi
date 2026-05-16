# IMPORT OPERATIONAL SYSTEM LIB TO WALK ON FOLDERS
import os
# IMPORT HASH LIB FOR IDENTIFY SHA AND MD5 PATTERNS
import hashlib
# IMPORT PATH LIB FOR WRAPPER PATHS
from pathlib import Path

# INPUT THE FOLDER WITH FILES TO MAKE SHA AND MD5 CODES
folder = './'
# CREATE INTEGRITY FOLDER TO STORAGE SHA OR MD5 LOG
os.mkdir('./integrity/')
# WALK IN THE FOLDER DIRECTORY, SUBFOLDERS AND FILES
for directory, subfolders, files in os.walk(folder):
    # SELECT EACH FILE
    for file in files:
        # CONVERT TO READBYTES PATTERNS
        filebytes = Path(os.path.join(directory, file)).read_bytes()
        # GET ENCODED SHA HASH CODE FROM FILE
        filehash_sha1 = hashlib.sha1(os.path.join(directory, file).encode())
        # GET ENCODED MD5 HASH CODE FROM FILE
        filehash_md5 = hashlib.md5(os.path.join(directory, file).encode())
        # CREATE FILE TO INPUT CODES
        f = open("integrity/sha.py", "a")
        # APPEND AND WRITE ON LOG FILE PATH AND HASH SHA CODE OF FILE
        f.write(' file:  '+((os.path.join(directory, file)+' \
        hash sha code: '+filehash_sha1.hexdigest()+'\n')))
        # CLOSE THE FILE
        f.close()
        # PRINT TO SEE INTEGRITY FILES CODES
        print((os.path.join(directory, file)+" "+filehash_sha1.hexdigest()))
