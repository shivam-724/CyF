from transformers import pipeline
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")

# Load Hugging Face emotion detection model
emotion_model = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)

# Load NLTK sentiment analyzer
sia = SentimentIntensityAnalyzer()

def analyze_emotion(text):
    """Detect dominant emotion and sentiment score"""
    emotion_scores = emotion_model(text)[0]
    top_emotion = max(emotion_scores, key=lambda x: x['score'])['label']
    
    sentiment_score = sia.polarity_scores(text)['compound']
    
    return {"emotion": top_emotion, "sentiment": sentiment_score}

if __name__ == "__main__":
    print(analyze_emotion("I feel so happy today!"))  # Should return "joy"
