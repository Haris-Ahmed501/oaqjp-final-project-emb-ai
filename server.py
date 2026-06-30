"""Flask server for the emotion detection application."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


APP = Flask(__name__)


@APP.route("/")
def home():
    """Render the home page of the application."""
    return render_template("index.html")


@APP.route("/emotionDetector")
def detect_emotion():
    """Detect emotions from user input and return the formatted response."""
    text_to_analyze = request.args.get("textToAnalyze")

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    response_text = (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']}, "
        f"and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_text


if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=5000)
