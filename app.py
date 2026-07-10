import os
import gradio as gr
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

personality = {
    "Teacher":"You are an experienced teacher. Answer questions like a teacher.",
    "Friend":"You are a friendly person. Answer casually and helpfully.",
    "Interviewer":"You are a technical interviewer.",
    "Student":"You are a student helping another student.",
    "Mentor":"You are a career mentor."
}

languages = {
    "english":"English",
    "kannada":"Kannada",
    "hindi":"Hindi"
}

def assistant(question, persona, language):

    system_instruction = f"{personality[persona]} Always answer in {languages[language]}."

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            temperature=1,
            max_output_tokens=3000
        ),
        contents=question
    )

    return response.text

demo = gr.Interface(
    fn=assistant,
    inputs=[
        gr.Textbox(lines=4,label="Question"),
        gr.Dropdown(list(personality.keys()),label="Persona"),
        gr.Dropdown(list(languages.keys()),label="Language")
    ],
    outputs=gr.Textbox(lines=10,label="Response"),
    title="Assistant PRO",
    description="Ask me anything!"
)

demo.launch(
    debug=True
)