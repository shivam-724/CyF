from fastapi import FastAPI
from pydantic import BaseModel
from analyze import analyze_emotion
from spotify_api import get_playlist

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/analyze-text/")
def analyze_text(data: TextInput):
    """Analyze text, detect emotion, and fetch a playlist"""
    analysis = analyze_emotion(data.text)
    emotion = analysis["emotion"]
    playlist_url = get_playlist(emotion)
    
    return {
        "emotion": emotion,
        "sentiment": analysis["sentiment"],
        "playlist": playlist_url
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
