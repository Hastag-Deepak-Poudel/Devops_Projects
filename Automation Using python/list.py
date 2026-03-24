import os, glob

if os.path.exists('FileManupulation'):
    contents = os.listdir('working with directories') # list all folders directory
    all_files = glob.glob("FileManupulation/*")
    print(contents,"\n")
    print(all_files)
    