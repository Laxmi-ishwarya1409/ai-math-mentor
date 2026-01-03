import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def speech_to_text(audio_path):
    with open(audio_path, "rb") as f:
        audio_bytes = f.read()

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=[
            {
                "role": "user",
                "parts": [
                    {"text": "Transcribe this audio accurately. Convert spoken math into correct symbols."},
                    {"inline_data": {"mime_type": "audio/wav", "data": audio_bytes}},
                ],
            }
        ],
    )

    return response.text
