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

    try:
        result = response.json()
    except Exception:
        return "OCR service failed. Please re-upload image or type the question."

    if not isinstance(result, dict):
        return "OCR service failed. Please re-upload image or type the question."

    if result.get("IsErroredOnProcessing"):
        return "Unable to read text from image."

    parsed = result.get("ParsedResults")
    if not parsed:
        return "Unable to read text from image."

    return parsed[0].get("ParsedText", "").strip()
