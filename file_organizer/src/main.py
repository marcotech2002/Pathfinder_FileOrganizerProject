# Library for operation system control
import os


# Navigate to the directory you want to organize
folder_path = (
    "file_organizer\\src\\folder_to_organize"
)
os.chdir(folder_path)

# Get a list of all files
all_files = [file for file in os.listdir() if os.path.isfile(file)]

# Create a set with each file type
files_types = {(file.split(".")[-1]).lower() for file in all_files}

# Create directories for each file type
for type in files_types:
    folder_name = type + "_files"
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

# Move files into their respective folders
for file in all_files:
    folder_path = (file.split(".")[-1]).lower() + "_files"
    origin = os.path.join(os.getcwd(), file)
    destination = os.path.join(os.getcwd(), folder_path, file)
    if os.path.exists(origin):
        os.replace(origin, destination)
print("Files organized successfully!")
