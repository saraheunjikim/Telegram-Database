import token_id
import boto3
import os

client = boto3.client('s3',
                      aws_access_key_id=token_id.access_key,
                      aws_secret_access_key=token_id.secret_access_key)


def upload_s3():
    for folder in os.listdir('C:/Users/Muffin/Desktop/python/projects/Telegram-Database/files'):
        path = 'C:/Users/Muffin/Desktop/python/projects/Telegram-Database/files'
        upload_file_bucket = 'telegram-data-saraheunjikim'

        if folder == 'corona':
            for file in os.listdir('C:/Users/Muffin/Desktop/python/projects/Telegram-Database/files/corona'):
                upload_file_key_txt = 'corona/' + str(file)
                client.upload_file(f'{path}/corona/{file}', upload_file_bucket, upload_file_key_txt)
                print(file + " uploaded")

        elif folder == 'jobs':
            for file in os.listdir('C:/Users/Muffin/Desktop/python/projects/Telegram-Database/files/jobs'):
                upload_file_key_txt = 'jobs/' + str(file)
                client.upload_file(f'{path}/jobs/{file}', upload_file_bucket, upload_file_key_txt)
                print(file + " uploaded")

    return True
