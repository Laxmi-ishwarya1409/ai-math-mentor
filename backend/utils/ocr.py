import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("K86299770688957")

def extract_text_from_image(image_path):
    with open(image_path, "rb") as f:
        response = requests.post(
            "https://api.ocr.space/parse/image",
            files={"filename": f},
            data={
                "apikey": API_KEY,
                "language": "eng",
                "isOverlayRequired": False,
            },
        )

    result = response.json()

    if result.get("IsErroredOnProcessing"):
        return "Unable to read text from image."

    return result["ParsedResults"][0]["ParsedText"].strip()
