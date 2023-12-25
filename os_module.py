# import os
# import shutil

# Reading from a File:
# file_path = 'file.txt'
# with open(file_path, 'r') as file:
#     content = file.read()
#     print(content)

# # Writing to a File:
# with open('new_file.txt', 'w') as file:
#     file.write('This is some text.')

# # Appending to a File:
# with open('existing_file.txt', 'a') as file:
#     file.write('\nThis is appended text.')

# # Checking if a File Exists:
# file_exists = os.path.exists('manju.txt')
# if file_exists:
#     print("File exists!")
# else:
#     print("File does not exist.")

# # Getting File Information (Size, Modification Time, etc.):
# file_info = os.stat('manju.txt')
# print("File Size:", file_info.st_size)  # File size in bytes
# print("Last Modified:", file_info.st_mtime)  # Last modified timestamp
# import datetime

# timestamp = 1703218283.826231
# converted_time = datetime.datetime.fromtimestamp(timestamp)

# print(converted_time)

# # Copying a File:
# shutil.copy('source_file.txt', 'destination_file.txt')

# Deleting a File:
# os.remove('mohit.txt')

# import os

# # Working with Files and Directories:

# Get the current working directory
# cwd = os.getcwd()
# print("Current working directory:", cwd)

# List files and directories in a specific path
# files = os.listdir(cwd)
# print("Files and directories in current directory:", files)

# Create a new directory
# new_dir = os.path.join(cwd, 'new_directory')
# os.mkdir(new_dir)

# Rename a file or directory
# os.rename('manju.txt', 'mohit.txt')

# # Delete a file
# os.remove('file_to_delete.txt')

# # Remove an empty directory
# os.rmdir('empty_directory')


# # Working with Paths:

# # Join paths (handles differences in path separators)
# path = os.path.join('folder', 'subfolder', 'file.txt')
# print("Joined path:", path)

# # Split path into directory name and file name
# dirname, filename = os.path.split(path)
# print("Directory name:", dirname)
# print("File name:", filename)

# # Get the file extension
# extension = os.path.splitext(path)[1]
# print("File extension:", extension)


# # Environmental Variables:

# # Get value of an environmental variable
# python_path = os.getenv('PYTHONPATH')
# print("Python path:", python_path)

# # Set an environmental variable
# os.environ['MY_VARIABLE'] = 'my_value'


# # Executing Operating System Commands:

# # Execute a shell command
# os.system('ls -l')

# f = open("manju.txt",'r')
# b=f.read()
# # file=f.write("\nnepal india pakistan srilanks")
# print(b)
# # print(file)

# with open("manju.txt",'r') as f:
#     print(f.read())
#     f.close()
