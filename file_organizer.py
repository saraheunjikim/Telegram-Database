import os
from os import listdir
import shutil

source_dir = 'C:/Users/Muffin/Desktop/python/projects/Telegram-Database/'
destination_dir = 'C:/Users/Muffin/Desktop/python/projects/Telegram-Database/files/'
files = [file for file in listdir(source_dir) if file.endswith('csv')]


# Get all file names in the directory
def file_names():
    files = [file for file in listdir(source_dir) if file.endswith('csv')]
    return files


# Read files and separate them
def categorize_files(files):
    for file in files:
        with open(file, mode='r', encoding='utf8') as f:
            text = f.readline().split(",")
        if 'Job ID' in text[0]:
            move_files(file, 'jobs/')
            f.close()
            print("This is a job related file")
        else:
            print("no")

    return True


# Move files
def move_files(file_name, category):
    print(file_name)
    print(category)
    return shutil.move(source_dir + file_name, destination_dir + category + file_name)


categorize_files(files)
