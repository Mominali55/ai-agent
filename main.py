import os
from dotenv import load_dotenv # locally stores in memeory the api key
from openai import OpenAI

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

if not api_key:
    raise RuntimeError("Key unable to fetch")

# Client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1", # Server change from defualt
    api_key=api_key
)

response = client.chat.completions.create(
    model="openrouter/free",
    messages=[
        {
            "role": "user",
            "content": "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
        }
    ],
)

print(response.choices[0].message.content)


if __name__ == "__main__":
    # main()

