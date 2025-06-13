import os
import requests
import base64
from datetime import datetime

def generate_krea_image(prompt: str) -> str:
    api_key = os.getenv("KREA_API_KEY")
    url = "https://api.krea.ai/v1/images/generate"
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {
        "prompt": prompt,
        "aspect_ratio": "1:1",
        "style": "cinematic"
    }

    response = requests.post(url, json=payload, headers=headers)
    image_base64 = response.json().get("image_base64")
    image_bytes = base64.b64decode(image_base64)

    filename = f"static/krea_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    os.makedirs("static", exist_ok=True)
    with open(filename, "wb") as f:
        f.write(image_bytes)

    return f"http://localhost:8000/{filename}"
