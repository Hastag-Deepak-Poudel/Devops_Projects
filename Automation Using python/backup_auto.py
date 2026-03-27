import shutil

def backup_folder(src,dst):
	shutil.copytree(src,dst) # Recursively copies all the files

# Enter the folder path which you want to backup
source_folder = input("Enter source fodler path: ")

# Enter the backup folder path you want to store backup folder
backup_folder = input("Enter backup folder path: ")

backup_folder(source_folder,backup_folder)
