import os
import shutil

path = "/Users/aryanagrwal/Documents/whitehat/python/C99"
source = "/Users/aryanagrwal/Documents/whitehat/python/C99/file.txt"
destination = "/Users/aryanagrwal/Documents/whitehat/python/C99/file1.txt"

dest = shutil.copy(source,destination)

print(os.listdir(path))