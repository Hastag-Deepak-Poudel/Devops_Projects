import os

filename = "movedfile.txt"

os.chmod(filename,0o444)


1. # Making a file read-only
2. # os.chmod(filename, 0o444) # for Linux-based systems
4. # Giving full permissions to the owner
5. # os.chmod(filename, 0o700) # for Linux-based systems