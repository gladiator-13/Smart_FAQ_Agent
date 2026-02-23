import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

MODEL_NAME="gemini-3-flash-preview"

def generate_response(prompt):
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
    )
    return response.text