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

v1.1.0
Created by Husamettin Eken                       
"""

def find_matching_files(file_extension):
    """Find all files with the given extension in current and subdirectories."""
    root_folder = os.getcwd()
    matching_files = []

    for foldername, _, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.endswith(file_extension):
                matching_files.append(os.path.join(foldername, filename))
    
    return matching_files

def compress_and_delete_files(matching_files):
    """Compress and delete the given list of files."""
    total_files = len(matching_files)

    for index, file_path in enumerate(matching_files, start=1):
        zip_path = file_path + ".zip"

        # Compress using ZIP_LZMA
        with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_LZMA) as zipf:
            zipf.write(file_path, os.path.basename(file_path))

        # Delete original file
        os.remove(file_path)
        print(f"[{index}/{total_files}] Compressed and deleted: {file_path}")

print(asciiart)

# Show current working directory
current_directory = os.getcwd()
print(f"Current working directory:\n{current_directory}")
print("All files in this directory and its subdirectories will be scanned.\n")

# Ask for file extension without the dot
file_extension = input("Enter the file extension to compress (e.g., bin, mp4): ").strip()

# Check if input is empty
if not file_extension:
    print("No file extension entered. Exiting program.")
else:
    # Add the dot before extension
    file_extension = "." + file_extension

    # Find matching files
    matching_files = find_matching_files(file_extension)
    total_files = len(matching_files)

    if total_files == 0:
        print(f"No '{file_extension}' files found. Exiting program.")
    else:
        # Ask for user confirmation with total file count
        answer = input(f"This process will compress and delete {total_files} '{file_extension}' files. Are you sure? (y/n): ").strip().lower()
        if answer == 'y':
            compress_and_delete_files(matching_files)
        elif answer == 'n':
            print("Operation canceled.")
        else:
            print("Invalid input! Please enter 'y' or 'n'.")

# Prevent the terminal from closing immediately
input("Press any key to continue...")
