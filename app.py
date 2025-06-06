from flask import Flask, request, jsonify

app = Flask(__name__)

image_lookup = {
    "sarcastic-bob": "https://raw.githubusercontent.com/VikVonnDoom/Project-Bob/main/SarcasticAnnoyedBob.png",
    "happy-bob": "https://raw.githubusercontent.com/VikVonnDoom/Project-Bob/main/HappyExcitedBob.png",
    "resting-bob": "https://raw.githubusercontent.com/VikVonnDoom/Project-Bob/main/RestingBobFace.png",
    "shocked-bob": "https://raw.githubusercontent.com/VikVonnDoom/Project-Bob/main/ShockedScaredBob.png",
    "chatty-bob": "https://raw.githubusercontent.com/VikVonnDoom/Project-Bob/main/ChattyBob.png"
}

@app.route("/get-image", methods=["GET"])
def get_image():
    mood = request.args.get("mood", "").lower()
    url = image_lookup.get(mood)

    if not url:
        return jsonify({
            "error": "Mood not found.",
            "valid_moods": list(image_lookup.keys())
        }), 404

    return jsonify({
        "mood": mood,
        "image_url": url
    })

if __name__ == "__main__":
    app.run(debug=True)
