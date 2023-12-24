import requests
import os

# Set your OpenAI API Key as an environment variable or insert it directly here
openai_api_key = os.environ.get("OPENAI_API_KEY", "")

# The OpenAI API URL for TTS
url = "https://api.openai.com/v1/audio/speech"

# Read text from a file
file_path = "input.txt"  # Replace with the path to your input file
with open(file_path, "r", encoding="utf-8") as file:
    text_content = file.read()

# The JSON payload for the API request
payload = {
    "model": "tts-1",
    "input": text_content,
    "voice": "alloy"
}

# Headers for the API request
headers = {
    "Authorization": f"Bearer {openai_api_key}",
    "Content-Type": "application/json",
}

# Send the POST request to the OpenAI API
response = requests.post(url, json=payload, headers=headers)

# Check for a successful response
if response.status_code == 200:
    # Save the response content to a file
    with open("speech.mp3", "wb") as file:
        file.write(response.content)
    print("Speech saved to speech.mp3")
else:
    print(f"Failed to generate speech: {response.status_code} - {response.text}")
