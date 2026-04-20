from EmotionDetection import emotion_detector

def test_emotions():
    test_cases = [
        ("I am glad this happened", "joy"),
        ("I am really mad about this", "anger"),
        ("I feel disgusted just hearing about this", "disgust"),
        ("I am so sad about this", "sadness"),
        ("I am really afraid that this will happen", "fear")
    ]

    for text, expected_emotion in test_cases:
        result = emotion_detector(text)
        detected_emotion = result['dominant_emotion']
        
        print(f"Text: {text}")
        print(f"Expected: {expected_emotion}, Detected: {detected_emotion}")
        
        assert detected_emotion == expected_emotion

    print("\nAll tests passed!")

if __name__ == "__main__":
    test_emotions()