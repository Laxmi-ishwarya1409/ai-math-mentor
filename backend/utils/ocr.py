import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def extract_text_from_image(image_path):
    with open(image_path, "rb") as f:
        image_bytes = f.read()

    image_part = types.Part.from_bytes(
        data=image_bytes,
        mime_type="image/png"
    )

    prompt = "Extract the math problem from this image. Return only the problem text."

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=[prompt, image_part]
    )

    return response.text.strip()
