from os import listdir

my_path = r'C:\Users\Muffin\Desktop\python\projects\Telegram-Database'


# Get all file names in the directory
def file_names():
    files = [file for file in listdir(my_path) if file.endswith('csv')]
    return files

files = [file for file in listdir(my_path) if file.endswith('csv')]
print(files)
# Open and read files
