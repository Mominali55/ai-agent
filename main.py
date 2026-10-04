import os
from dotenv import load_dotenv # locally stores in memeory the api key
from openai import OpenAI
import argparse


load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

if not api_key:
    raise RuntimeError("Key unable to fetch")

# Client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1", # Server change from defualt
    api_key=api_key
)

# Parser object creation
parser = argparse.ArgumentParser(description="Ai chat bot")
parser.add_argument("user_prompt",type=str,help="Enter user prompt")
args = parser.parse_args()


response = client.chat.completions.create(
    model="openrouter/free",
    messages=[
        {
            "role": "user",
            "content": args.user_prompt
        }
    ],
)


if not response.usage:
    raise RuntimeError("Failed API request")

# Model output info
print(f"""User prompt: {args.user_prompt}
Prompt tokens: {response.usage.prompt_tokens}
Response tokens: {response.usage.completion_tokens}
Response:
{response.choices[0].message.content}""")

