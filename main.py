# Standard libraries
import os
import argparse
# Third-Party libraries
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    # Use argparse library to get user prompt as a command-line argument
    parser = argparse.ArgumentParser(description="Gemini code assistant")
    parser.add_argument("user_prompt", type=str, help="Add user prompt to send to Gemini - use quotes")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    # Setup - load environment variables, validate API key
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("Gemini API key is missing")
    
    # Prep  - Initialize AI client and convo history
    client = genai.Client(api_key=api_key)
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    # Start chat
    generate_chat(client, messages, args)

# API request/response cycle
def generate_chat(client, messages, args):
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = messages
    )

    # Check for API resquest error - did we receive data back?
    if response.usage_metadata is None:
        raise RuntimeError("Failed API request")
    
    if args.verbose is True:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    print("Gemini response:")
    print(response.text)


if __name__ == "__main__":
    main()
