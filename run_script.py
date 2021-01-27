import file_organizer
import upload_to_s3
import subprocess

# subprocess.Popen(['C:/Users/Muffin/Desktop/python/projects/Telegram-Database/telegram_get.py'])
# subprocess.Popen(['C:/Users/Muffin/Desktop/python/projects/Telegram-Database/file_trigger.py'])


subprocess.call(['python.exe', 'telegram_get.py', 'file_trigger.py'])
