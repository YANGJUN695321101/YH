import os
import json
import requests
import openai
import os
import os
from dotenv import load_dotenv
from config_key import get_api_key



API_KEY = get_api_key()


API_URL = "https://api.openai.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

def generate_gpt35_response(prompt):
    model_engine = "gpt-3.5-turbo"
    
    data = {
        "model": model_engine,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    response = requests.post(API_URL, headers=headers, data=json.dumps(data))
    response_data = response.json()

    if response.status_code == 200:
        message = response_data['choices'][0]['message']['content'].strip()
        return message
    else:
        print("Error:", response_data)
        return None
