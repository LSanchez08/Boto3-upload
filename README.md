# Boto3-upload

## backup.py

1. pip install boto3
2. python backup.py {source} {bucket} {AWS_ACCESS_KEY_ID}:@:{AWS_SECRET_ACCESS_KEY}

Note: I added an extra parameter to the script for terms of, the credentials will be shared in the email alongside the name of the repository used for testing (In case they are needed).

## noCredentials.py

Non-functional version of the code without the section to obtain credentials from the shell params. 