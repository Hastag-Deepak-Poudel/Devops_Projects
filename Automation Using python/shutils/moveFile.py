import shutil

source = "movedfile.txt"
destination = "FileManupulation/"

shutil.move(source,destination)
print(f"File moved from {source} to {destination}")