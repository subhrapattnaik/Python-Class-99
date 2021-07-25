#shutil.copy() method
import shutil
source="C:/Python/99/file1.txt"
destination="C:/Python/99/folder1/folder2/file1.txt"

try:
    #shutil.copy(source,destination)
    print("File copied successfully")

except shutil.SameFileError:
    print("Source and destination represents the same file.")

except PermissionError:
    print("Permission denied")
except:
    print("Error occurred while copying file")

#-------------------------------------------------------------

#to know the permission of the file
import os
source="C:/Python/99/abc.txt"
perm=os.stat(source).st_mode
print(perm)

#---------------------------------------------
#if destination is a directory
import os
import shutil
source="C:/Python/99/folder1/folder2/file1.txt"
destination="C:/Python/99/myfolder2"
#dest=shutil.copy(source,destination)

print(os.listdir(destination))
#print("destination path:",dest)
#------------------------------------------------
#---------------------------------------------------

#shutil.move() method
#moves file from source to destination
import os
import shutil

path="C:/Python/99/folder1"
print("Before moving files: ")
print(os.listdir(path))

#moves folder(folder2 with its content --to the destination folder)
source="C:/Python/99/folder1/folder2"
destination="C:/Python/99/backupfolder"

#dest=shutil.move(source,destination)

print("Before moving files: ")
print(os.listdir(path))
#--------------------------------------------------

#shutil.copyfile
#copy the contents of the source file to destination file

source="C:/Python/99/file.txt"
destination="C:/Python/99/backupfolder/folder2/file1.txt"

dest=shutil.copyfile(source,destination)
#-----------------------------------------
import shutil

source="C:/Python/99/file.txt"
destination="C:/Python/folder1"

try:
   shutil.copyfile(source,destination)
   print("file copied successfully")
except shutil.SameFileError:
    print("source and destination represents the same file")
except IsADirectoryError:
    print("destination is a directory")
except PermissionError:
    print("Permission denied")
except:
    print("Error occurred while copying file")

#------------------------------------------------------




