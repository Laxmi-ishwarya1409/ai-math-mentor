import os
import base64
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def extract_text_from_image(image_path):
    with open(image_path, "rb") as f:
        image_bytes = f.read()

    encoded = base64.b64encode(image_bytes).decode("utf-8")

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=[
            {
                "role": "user",
                "parts": [
                    {"text": "Extract the math problem from this image. Return only the problem text."},
                    {
                        "inline_data": {
                            "mime_type": "image/png",
                            "data": encoded
                        }
                    },
                ],
            }
        ],
    )

    return response.text.strip()
