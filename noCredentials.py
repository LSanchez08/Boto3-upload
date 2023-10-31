import boto3
from datetime import date
import os
import platform
import shutil
import sys

path = False
def main ():
  global destination
  global filename
  global source
  global s3 
  try:
    source = sys.argv[1] # Obtaining source directory
    destination = sys.argv[2] # Obtaining destination bucket 
  except: # If not all arguments are passed
    print('Source directory and destination bucket are required')
    return

  

  path = os.path.isdir(source) # Checking if source directory is valid
  if (path == False):
    print('Invalid Source directory')
    return


  try:
    filename = source.split('/')[-1] # Obtaining filename from source directory last folder
    shutil.make_archive(filename, 'zip', source) # Zipping source directory using shutil
  except: # If error occures while zipping
    print('Invalid directory contents')

  try: # Connecting to S3
    s3 = boto3.client(
    's3',
    aws_access_key_id= 'ACCESS_KEY',
    aws_secret_access_key= 'SECRET_KEY'
    )
  except: # If error occures while connecting to S3
    print('Error connecting to S3')
    return

  try:
    response = s3.upload_file(f'{filename}.zip', destination, f'{str(date.today())}/{filename}.zip') # Uploading file to S3 on a directory named after the current date
    print('File uploaded to S3')
  except: # If error occures while uploading to S3
    print('Error uploading file to S3')
    return
  


main()
