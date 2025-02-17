import streamlit as st
import requests

st.title("🎶 Emotion-Based Playlist Generator")
st.write("Enter your feelings below, and we'll suggest a playlist!")

user_text = st.text_area("Describe how you're feeling:")

if st.button("Get Playlist"):
    if user_text:
        response = requests.post("http://127.0.0.1:8000/analyze-text/", json={"text": user_text})
        data = response.json()
        st.write(f"**Detected Emotion:** {data['emotion']}")
        st.write(f"**Sentiment Score:** {data['sentiment']}")
        st.markdown(f"[🎵 Listen to Playlist]({data['playlist']})")
    else:
        st.warning("Please enter some text.")
