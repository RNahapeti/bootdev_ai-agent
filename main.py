# Standard libraries
import os
import argparse
# Third-Party libraries
from dotenv import load_dotenv
from google import genai

def main():
    # Use argparse library to get user prompt as a command-line argument
    parser = argparse.ArgumentParser(description="Gemini code assistant")
    parser.add_argument("user_prompt", type=str, help="Add user prompt to send to Gemini - use quotes")
    args = parser.parse_args()

    # Authentication - retrieve API key and initializ connection to Google servers
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("Gemini API key is missing")
    client = genai.Client(api_key=api_key)

    # API request - use specific model and pass on user prompt
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = args.user_prompt
    )

    # Check for API resquest error - did we receive data back?
    if response.usage_metadata is None:
        raise RuntimeError("Failed API request")
    
    # Output
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print("Gemini response:")
    print(response.text)


if __name__ == "__main__":
    main()
