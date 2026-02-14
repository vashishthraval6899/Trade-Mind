import requests
import os

OPENROUTER_API_KEY = os.getenv("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")

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

def query_llm(prompt):

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": "https://trademind.app",   # REQUIRED
        "X-Title": "TradeMind",                   # REQUIRED
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3
    }

    response = requests.post(OPENROUTER_URL, headers=headers, json=data)

    if response.status_code != 200:
        print("STATUS:", response.status_code)
        print("RESPONSE:", response.text)
        raise Exception("OpenRouter API Error")

    return response.json()["choices"][0]["message"]["content"]
