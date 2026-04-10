print("HELLO - SCRIPT IS RUNNING")
# Assignemnt 4: Github.py

# Author - Michal Gondek

import requests 
import base64   
from config import config as cfg
token = cfg['githubkey']

# Details of Repository
owner = "MichalGondek"
repo = "WSAA-coursework"
path = 'assignments/test.txt' 

url = f"https://api.github.com/repos/MichalGondek/WSAA-coursework/contents/assignments/test.txt"

headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github+json"
}

# Get File From Repository
response = requests.get(url, headers=headers)

if response.status_code != 200:
    print('Error getting file', response.status_code)
    exit()

file_data = response.json()

# Decode the file content
content = base64.b64decode(file_data['content']).decode('utf-8')

# Replace Andrew with Michal
new_content = content.replace('Andrew', 'Michal')
if 'Andrew' in content:
    new_content = content.replace('Andrew', 'Michal')
    print('Replacement done')
else:
    print('No Andrew found in the file')

# Encode updated content
encoded_content = base64.b64encode(new_content.encode('utf-8')).decode('utf-8')

# Commit and push changes back to GitHub
data = {
    'message': 'Assignemnt04: replaced Andrew with Michal',
    'content': encoded_content,
    'sha': file_data['sha']
}

put_response = requests.put(url, headers=headers, json=data)
if put_response.status_code == 200:
    print('File updated successfully')
else:
    print('Error updating file', put_response.status_code)
    