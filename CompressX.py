import os
import zipfile

asciiart = """
   _____                                       __   __
  / ____|                                      \ \ / /
 | |     ___  _ __ ___  _ __  _ __ ___  ___ ___ \ V / 
 | |    / _ \| '_ ` _ \| '_ \| '__/ _ \/ __/ __| > <  
 | |___| (_) | | | | | | |_) | | |  __/\__ \__ \/ . \ 
  \_____\___/|_| |_| |_| .__/|_|  \___||___/___/_/ \_\\
                       | |                            
                       |_|                            

v1.0.0
Created by Husamettin Eken                       
"""



def compress_and_delete_files(file_extension):
    root_folder = os.getcwd()  # Current working directory

    for foldername, _, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.endswith(file_extension):
                file_path = os.path.join(foldername, filename)
                zip_path = file_path + ".zip"
                
                # Compress using ZIP_LZMA
                with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_LZMA) as zipf:
                    zipf.write(file_path, filename)
                
                # Delete original file
                os.remove(file_path)
                print(f"Compressed and deleted: {file_path}")

print(asciiart)

# Ask for file extension without the dot
file_extension = input("Enter the file extension to compress (e.g., bin, mp4): ").strip()

# Add the dot before extension
file_extension = "." + file_extension

# Ask for user confirmation
answer = input(f"This process will delete all {file_extension} files after compression! Are you sure? (y/n): ").strip().lower()
if answer == 'y':
    compress_and_delete_files(file_extension)
elif answer == 'n':
    print("Operation canceled.")
else:
    print("Invalid input! Please enter 'y' or 'n'.")

# Prevent the terminal from closing immediately
input("Press any key to continue...")
