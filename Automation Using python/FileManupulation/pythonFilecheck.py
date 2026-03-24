import os

filename = "example2.txt"

if os.path.exists(filename):
    print(f"{filename} exists")
else:
    print(f"{filename} doesnot exists")