import gradio as gr
from mood_detector import detect_mood 
from recommender import recommend_video


def chatbot_response(user_input):
    mood = detect_mood(user_input)
    video = recommend_video(mood)
    return f"Detected Mood:**{mood}**\n\n Suggested Video: {video}" 

gr.Interface(fn = chatbot_response,inputs="text",outputs="markdown",
             title = "Mental health Companion Bot",
             description = "Describe how you feel and get helpful suggestions.").launch()
