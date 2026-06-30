from EmotionDetection.emotion_detection import emotion_detector

def test_emotion_detector_joy():
    result = emotion_detector("I am glad this happened")
    assert result["dominant_emotion"] == "joy"

def test_emotion_detector_anger():
    result = emotion_detector("i am really mad about this")
    assert result["dominant_emotion"] == "anger"

def test_emotion_detector_disgust():
    result = emotion_detector("i feel disgusted just hearing about this")
    assert result["dominant_emotion"] == "disgust"

def test_emotion_detector_sadness():
    result = emotion_detector("I am so sad about this")
    assert result["dominant_emotion"] == "sadness"

def test_emotion_detector_fear():
    result = emotion_detector("i am really afraid that this will happen")
    assert result["dominant+emotion"] == "fear"