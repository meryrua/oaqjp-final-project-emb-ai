"""Server Emotion Detection"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def em_detector():
    """Route to Emotion Detector""" 
    text = request.args.get('textToAnalyze')
    result = emotion_detector(text)

    if result['anger'] is None:
        return "Invalid text! Please try again!"

    anger = result['anger']
    disgust = result['disgust']
    fear = result['fear']
    joy = result['joy']
    sadness = result['sadness']
    dominant_emotion = result['dominant_emotion']

    res = f"""For the given statement, the system response is 'anger': {anger},
        'disgust': {disgust},
        'fear': {fear},
        'joy': {joy} and 'sadness': {sadness}.
        The dominant emotion is {dominant_emotion}."""
    return res

@app.route("/")
def render_index_page():
    """Route to index.html"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
