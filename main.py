import os
import json
import requests

access_token = os.getenv('access_token')
project_id = os.getenv("project_id")

url = "https://texttospeech.googleapis.com/v1/text:synthesize"


headers = {
    "Authorization": f"Bearer {access_token}",
    "x-goog-user-project": f"{project_id}",
    "Content-Type": "application/json; charset=utf-8"
}

data = {
    "input": {
        "text": "I've added the event to your calendar."
    },
    "voice": {
        "languageCode": "en-gb",
        "name": "en-GB-Standard-A",
        "ssmlGender": "FEMALE"
    },
    "audioConfig": {
        "audioEncoding": "MP3"
    }
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.json())

