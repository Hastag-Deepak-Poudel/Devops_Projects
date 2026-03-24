import os
import shutil

def origanize_files(folder_path):
    extensions_folder = {
        '.txt':'TextFiles',
        '.pdf':'Document',
        '.png':'Images',
        '.jpg':'Images',
    }
    for filename in os.listdir(folder_path):
        file_extension = os.path.splitext(filename)[1]
        directory = extensions_folder.get(file_extension)
        if directory:
            target_directory = os.path.join(folder_path, directory)
            if not os.path.exists(target_directory):
                os.mkdir(target_directory)
                shutil.move(os.path.join(folder_path,filename), os.path.join(target_directory,filename))
        
        else:
            other_dir = os.path.join(folder_path,'others')

            if not os.path.exists(other_dir):
                os.mkdir(other_dir)
                
            source = os.path.join(folder_path,filename)
            destination = os.path.join(other_dir,filename)

            shutil.move(source,destination) 

folder_path = input("Enter folder path: ")
origanize_files(folder_path)
