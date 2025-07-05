from transformers import pipeline

# Loading pretrained emotion classification model

emotion_model = pipeline("sentiment-analysis",model="bhadresh-savani/distilbert-base-uncased-emotion")

def detect_mood(text):
    result = emotion_model(text)[0]
    return result["label"]