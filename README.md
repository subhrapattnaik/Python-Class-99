
# Python-Class-99

https://www.askpython.com/python-modules/shutil-module



shutil.copy() method in Python is used to copy the content of the source file to the destination file or directory. It also preserves the file’s permission mode but other metadata of the file like the file’s creation and modification times is not preserved.
The source must represent a file but the destination can be a file or a directory. If the destination is a directory then the file will be copied into the destination using the base filename from the source. Also, the destination must be writable. If the destination is a file and already exists then it will be replaced with the source file otherwise a new file will be created.


Example:


# Python program to explain shutil.copy() method 
  
# importing shutil module 
import shutil 
  
source = "path/main.py"
destination ="path/main2.py"
  
# Copy the content of 
# source to destination 
dest = shutil.copy(source, destination) 
  
# Print path of newly 
# created file 
print("Destination path:", dest) 




#------------------------------------------------------
shutil.copy2() method in Python is used to copy the content of the source file to the destination file or directory. This method is identical to shutil.copy() method but it also tries to preserve the file’s metadata.

Example:

source = "csv/main.py"
  
# Print the metadeta 
# of source file 
metadata = os.stat(source) 
print("Metadata:", metadata, "\n") 
  
# Destination path 
destination = "csv/gfg/check.txt"
  
# Copy the content of 
# source to destination 
dest = shutil.copy2(source, destination) 

 Print the metadata 
# of the destination file 
matadata = os.stat(destination) 
print("Metadata:", metadata) 

----------------------------------------------------------------------------

shutil.copyfile() method in Python is used to copy the content of the source file to the destination file. The metadata of the file is not copied. Source and destination must represent a file and destination must be writable. If the destination already exists then it will be replaced with the source file otherwise a new file will be created.

Example:
# Source path 
source = "csv/main.py"
  
# Destination path 
destination = "csv/gfg/main_2.py"
  
dest = shutil.copyfile(source, destination) 
  
print("Destination path:", dest) 

-----------------------------------------------------------------------
shutil.copytree() method recursively copies an entire directory tree rooted at source (src) to the destination directory. The destination directory, named by (dst) must not already exist. It will be created during copying.


Example:

src = 'C:/Users/ksaty/csv/gfg'
  
# Destination path 
dest = 'C:/Users/ksaty/csv/gfg/dest'
  
# Copy the content of 
# source to destination 
destination = shutil.copytree(src, dest) 
  

-----------------------------------------------------------------------

shutil.rmtree() is used to delete an entire directory tree, the path must point to a directory (but not a symbolic link to a directory).

Example:
location = "csv/gfg/"
  
# directory 
dir = "dest"
  
# path 
path = os.path.join(location, dir) 
  
# removing directory 
shutil.rmtree(path) 

-----------------------------------------------------------------------

The shutil module helps you automate copying files and directories. This saves the steps of opening, reading, writing and closing files when there is no actual processing, simply moving files.

shutil. copy ( src , dest )
Copy data and mode bits, basically the unix command cp src dst. If dest is a directory, a file with the same base name as src is created. If dest is a full file name, this is the destination file.

shutil.copyfile ( src , dest )
Copy data from src to dest . Both names must be files.

shutil.copytree ( src , dest )
Recursively copy the entire directory tree rooted at src to dest . dest must not already exist. Errors are reported to standard output.

shutil.rmtree ( path )
Recursively delete a directory tree rooted at path .
