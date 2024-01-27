""""
This module practice working with OS Module.
"""

import os

# Show all the metods in os module
# print(dir(os))

# Get current work dir
print(os.getcwd())

# Change current work dir
os.chdir("E:\Hamid\Projects")
print(os.getcwd())

# Show all dirs in current work dir
print(os.listdir())

# Create directory in current work dir
# os.mkdir("test_dir") # Can just create one level directory
os.makedirs("test_dir/sub_dir") # Can create multi level directory

# Remove directory from current work dir
# os.rmdir("test_dir") # Can just remove one level directory
os.removedirs("test_dir/sub_dir") # Can remove multi level directory

# Rename directory or file in current work dir
# os.mkdir("test_dir")
# os.rename("test_dir", "test_directory")
print(os.listdir())

# Get some info about file
# os.stat("filename.txt")

os.chdir("E:\Hamid\Projects\python-tutorial")
# Show tree mode of directories and files
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print("Dir Path:", dirpath)
    print("Directories:", dirnames)
    print("Files:", filenames)
    print()

# Get "ANDROID_HOME" environment variable path
env_path = os.environ.get("ANDROID_HOME")
# Join two path
print(os.path.join(env_path, "test.txt"))

# Working with some of important attributes of path meyhod of os module
print(os.path.exists("C:\sdk\\test.txt"))
print(os.path.isdir("C:\sdk\\test.txt"))
print(os.path.isfile("C:\sdk\\test.txt"))
print(os.path.basename("C:\sdk\\test.txt"))
print(os.path.dirname("C:\sdk\\test.txt"))
print(os.path.split("C:\sdk\\test.txt"))
print(os.path.splitext("C:\sdk\\test.txt"))
