import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_joke():
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": "ספר לי בדיחה קצרה ומצחיקה"}
        ]
    )
    return response.choices[0].message["content"]

if __name__ == "__main__":
    print(get_joke())
