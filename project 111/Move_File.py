import os
import shutil

from_dir = "Downloads"
to_dir = "Document_Files"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    file_name, file_extension = os.path.splitext(file_name)
    