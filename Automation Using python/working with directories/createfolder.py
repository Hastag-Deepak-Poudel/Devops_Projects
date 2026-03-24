import os

if not os.path.exists('newFolder'):
    os.mkdir('newFolder')  # Creates new folder


if os.path.exists("newFolder"):
    os.chdir('newFolder')   #changes directory to newFolder
    if not os.path.exists('2newFolder'):
        os.mkdir('2newFolder') # Create 2newFolder directory inside newFolder


if os.path.exists('2newFolder'):
    os.rmdir('2newFolder')  # deletes directory
