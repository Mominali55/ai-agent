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
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

# User messages stored
messages=[
    {"role": "user", "content": args.user_prompt},
]

def generate_content(client: OpenAI,messages: list)-> None:
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
    )
    if not response.usage:
        raise RuntimeError("Failed API request")

    # Model output info
    ## Verbose included True
    if args.verbose:
        print(f"""
        User prompt: {args.user_prompt}
        Prompt tokens: {response.usage.prompt_tokens}
        Response tokens: {response.usage.completion_tokens}""")

    ## If not verbose
    print(f"""
    Response:
    {response.choices[0].message.content}""")


# Call 1
generate_content(client,messages)


