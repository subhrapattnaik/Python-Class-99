#The os module in python provides functions for interacting with the operating system
#The os and os.path modules include many functions to interact with the file system

import os
#get the current working directory
cwd=os.getcwd()
print(cwd)

#os.chdir() method is used to change the cwd to a specified path
#os.chdir('../')
#cwd=os.getcwd()
#print(cwd)
#--------------------------------------------------------------------
#creating directory
#os.mkdir() method is used to create a directory ,error comes if the directory already exists
import os
directory="subhrafolder"
parent_dir="C:/Python/99"
path=os.path.join(parent_dir,directory)
#os.mkdir(path)
print("Directory '% s' created "% directory)

#----------------------------------------------------------------------------------------
#os.makedirs()
#os.makedirs() method in python is used to create a directory recursively
#that means while creating leaf directory , if any intermediate directory is missing,os.makedirs() method will create them all

#leaf directory
directory="c"
parent_dir="C:/Python/99/a/b"

mode=0o666
path=os.path.join(parent_dir,directory)
#create the directory 'c'
#os.makedirs(path,mode)
print("Directory '%s' created "% directory)
#-----------------------------------------------------------------
#listing out files and directories with python
#os.listdir() method is used to get the list of all files and directories in the specified directory
#if we don't specify any directory, then takes from current directory

import os
path="C:/Python/99"
dir_list=os.listdir(path)
print("Files and directories in ",path , ":")
print(dir_list)

#deleting directory or files using python
#os.remove() method used to remove a file path(cannot remove a directory.OSERROR comes is we try)
os.chdir('C:/Python/99')
cwd=os.getcwd()
print(cwd)


import os
file='file1.txt'
location="C:/Python/99/"
path=os.path.join(location,file)
#os.remove(path)

#os.rmdir() method is used to remove or delete an empty directory
#OSERROR will be raised if not an empty directory

import os
directory="subhrafolder1"
parent="C:/Python/99"
path=os.path.join(parent,directory)
#os.rmdir(path)

#os.name gives the name of the operating system
import os
print(os.name)


import os
try:
    #if the file doesnot exists, then it would throw an error
    filename="GFD.txt"
    f=open(filename,'rU')
    text=f.read()
    f.close()

except IOError:
    print("Problem in reading " + filename)

#-------------------------------------------------

#popen() provides a pipe or gateway and access the file directly
#popen() is similar to open()
#Output for popen() will not be shown ,there would be direct changes into the file

import os
fd="abc.txt"
file=open(fd,'w')
file.write("Hello Hi")
file.close()

file=open(fd,'r')
text=file.read()
print(text)

file=os.popen(fd,'w')
file.write("Hello")

#------------------------------------------------------------

#os.close()

#os.path.exists(filename)  tells file exists or not -----------------------
import os
result=os.path.exists("abc.txt")
print(result)
#____________________________________________

#os.walk()
#this method generates the filenames in a directory tree by walking the tree in either a top-down or bottom-up manner.
#os.walk returns a generator that creates a tuple of values(dirpath,dirnames,filenames)

#for dirpath,dirnames,filenames in os.walk("C:/Python/99"):
    #print(dirpath)
    #print(dirnames)
    #print(filenames)

#-----------------------------------------

#os.path.join()
#joins various path components
#base_path="C:/Python/99/"
#print(base_path)
#new_path=os.path.join(base_path,"newfolder")
#print(new_path)



#os.path.split()
#this method is used to split the pathname into a pair of head and tail
#here tail is the last pathname component and the head is everything that comes before it.
#this method returns a tuple of head and tail of the specified path


os.path.split("C:/Python/99/newfolder")
#--------------------------------------
#checking access

path1=os.access("C:/Python/99/abc.txt",os.F_OK)
path1=("Exists path : ",path1)
print(path1)


path2=os.access("C:/Python/99/abc.txt",os.R_OK)
path2=("it access to read the file  : ",path2)
print(path2)


path3=os.access("C:/Python/99/abc.txt",os.W_OK)
path3=("it access to write the file : ",path3)
print(path3)

path4=os.access("C:/Python/99/abc.txt",os.X_OK)
path4=("check if path can be executed : ",path1)
print(path4)

#------------------------------------------
#rename a folder
#os.rename("oldfoldername","newfoldername")
#os.rename("myfolder","myfolder2")
#------------------------------------------------



