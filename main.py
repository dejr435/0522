from flask import Flask, request, jsonify
from generate_krea import generate_krea_image
from generate_dalle import generate_dalle_image

app = Flask(__name__)

@app.route("/generate", methods=["POST"])
def generate_image():
    data = request.get_json()
    prompt = data.get("prompt")
    model = data.get("model", "krea")

    if not prompt:
        return jsonify({"status": "error", "message": "Missing prompt"}), 400

    if model == "krea":
        image_url = generate_krea_image(prompt)
    elif model == "dalle3":
        image_url = generate_dalle_image(prompt)
    else:
        return jsonify({"status": "error", "message": "Unsupported model"}), 400

    return jsonify({
        "status": "success",
        "model": model,
        "image_url": image_url
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
