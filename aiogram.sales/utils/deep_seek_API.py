import requests
import json

import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY_DEEPSEEK")

MODEL = "deepseek/deepseek-chat"

def process_content(content):
    return content.replace('<think>', '').replace('</think>', '')
def chat_stream(prompt):
    if not API_KEY:
        raise ValueError("API_KEY_DEEPSEEK not found in environment variables")
        
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "stream": True
    }

    with requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=data,
        stream=True,
        timeout=30  # Add timeout
    ) as response:
        response.raise_for_status()  # Raise exception for bad status codes
        if response.status_code != 200:
            print("Ошибка API:", response.status_code)
            return ""

        full_response = []
        
        for chunk in response.iter_lines():
            if chunk:
                chunk_str = chunk.decode('utf-8').replace('data: ', '')
                try:
                    chunk_json = json.loads(chunk_str)
                    if "choices" in chunk_json:
                        content = chunk_json["choices"][0]["delta"].get("content", "")
                        if content:
                            cleaned = process_content(content)
                            print(cleaned, end='', flush=True)
                            full_response.append(cleaned)
                except:
                    pass

        print()
        return ''.join(full_response)
def main():
    print("Чат с DeepSeek-chat (by Antric)\nДля выхода введите 'exit'\n")

    while True:
        user_input = input("Вы: ")
        
        if user_input.lower() == 'exit':
            print("Завершение работы...")
            break
            
        print("DeepSeek-chat:", end=' ', flush=True)
        chat_stream(user_input)

if __name__ == "__main__":
    main()