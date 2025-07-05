mood_video_map = {
    "sad": "https://youtu.be/ZToicYcHIOU",  # meditation
    "joy": "https://youtu.be/GXoErccq0vw",  # happy
    "anger": "https://youtu.be/tYzMYcUty6s",  # calm down
    "fear": "https://youtu.be/O-6f5wQXSu8",  # relax
    "surprise": "https://youtu.be/1vx8iUvfyCY",
    "love": "https://youtu.be/ysSxxIqKNN0"
}

def recommend_video(mood):
    return mood_video_map.get(mood.lower(),"https://youtube.com")