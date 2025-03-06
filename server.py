from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def em_detector():
    text = request.args.get('textToAnalyze')
    result = emotion_detector(text)

    anger = result['anger']
    disgust = result['disgust']
    fear = result['fear']
    joy = result['joy']
    sadness = result['sadness']
    dominant_emotion = result['dominant_emotion']

    res = """For the given statement, the system response is 'anger': {}, 
        'disgust': {}, 
        'fear': {}, 
        'joy': {} and 'sadness': {}. 
        The dominant emotion is {}.""".format(anger, disgust, fear, joy, sadness, dominant_emotion)
    return res

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
