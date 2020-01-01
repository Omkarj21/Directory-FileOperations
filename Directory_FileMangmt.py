import os
# get the present working directory using the getcwd() method
print(os.getcwd())
# use the getcwdb() method to get it as bytes object
print(os.getcwdb())
# All files and sub directories inside a directory can be known using the listdir() method
print(os.listdir())
print(os.listdir('D:\\'))
# make a new directory using the mkdir() method
os.mkdir('NewFolder')
# rename() method can rename a directory or a file
os.rename('NewFolder','NewFolderAgain')
# change the current working directory using the chdir() method
os.chdir(r'D:\Omkar Personal\Career\File Operations\NewFolderAgain')
print(os.getcwd())
# remove file using the remove() method from working directory
os.remove('Hello.txt')
# remove only empty directories using this method
os.rmdir('NewFolderAgain')
# In order to remove a non-empty directory we can use the rmtree() method inside the shutil module.
import shutil
shutil.rmtree('NewFolderAgain')