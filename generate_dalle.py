import os
import openai
import requests
from datetime import datetime

def generate_dalle_image(prompt: str) -> str:
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    image_data = requests.get(image_url).content

    filename = f"static/dalle_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    os.makedirs("static", exist_ok=True)
    with open(filename, "wb") as f:
        f.write(image_data)

    return f"http://localhost:8000/{filename}"
