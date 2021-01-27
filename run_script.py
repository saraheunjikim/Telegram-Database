import telegram_get
import file_organizer
import file_trigger
import upload_to_s3


# 1. run telegram_get.py to get files
telegram_get.execute_chat()

# 2. run file_organizer.py to sort files
files = file_organizer.file_names()
file_organizer.categorize_files(files)

# 3. Upload the files to S3 bucket
upload_to_s3.upload_s3()

# 4. Process the files using AWS Lambda

# 5. Move the files to AWS RedShift


#
