import os, time

filename = "new_text.txt"
fileSize = os.path.getsize(filename)

print(f"The size of {filename} is {fileSize}, which is in bytes.")


# modification time of a file

filemod = os.path.getmtime(filename)
readable_time = time.ctime(filemod)

print(f"The last time {filename} was modified is {readable_time}")