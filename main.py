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

user_prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
response = client.chat.completions.create(
    model="openrouter/free",
    messages=[
        {
            "role": "user",
            "content": user_prompt,
        }
    ],
)


if not response.usage:
    raise RuntimeError("Failed API request")

# Model output info
print(f"""User prompt: {user_prompt}
Prompt tokens: {response.usage.prompt_tokens}
Response tokens: {response.usage.completion_tokens}
Response:
{response.choices[0].message.content}""")

