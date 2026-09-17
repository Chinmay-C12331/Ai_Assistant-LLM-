
# 🤖 Assistant PRO – AI Assistant LLM

Assistant PRO is an AI-powered conversational assistant built using Google's Gemini 2.5 Flash model and Gradio. It allows users to ask questions, select different assistant personas, and receive responses in their preferred language.

The application is deployed publicly using Render.

## 🚀 Live Demo

🔗 [Try Assistant PRO](https://ai-assistant-llm-a7v1.onrender.com)

## ✨ Features

- 🤖 AI-powered question answering using Gemini 2.5 Flash
- 👨‍🏫 Multiple assistant personas:
  - Teacher
  - Friend
  - Interviewer
  - Student
  - Mentor
- 🌐 Multilingual responses:
  - English
  - Kannada
  - Hindi
- 💬 Interactive web interface using Gradio
- ⚙️ Custom system instructions based on persona and language
- 🚀 Public deployment using Render
- 🔐 API key management using environment variables

## 🛠️ Technologies Used

- **Programming Language:** Python
- **AI Model:** Google Gemini 2.5 Flash
- **AI SDK:** Google Gen AI SDK
- **Frontend / UI:** Gradio
- **Environment Management:** python-dotenv
- **Deployment:** Render

## 📂 Project Structure

```text
Ai_Assistant-LLM-/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

> The filenames above are examples. Update them according to your actual repository structure.

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Chinmay-C12331/Ai_Assistant-LLM-.git
cd Ai_Assistant-LLM-
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment on Windows:

```powershell
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the API Key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Never upload your API key to GitHub.

### 5. Run the Application

```bash
python app.py
```

The Gradio application will run locally.

## 🧠 How It Works

1. The user enters a question.
2. The user selects an assistant persona.
3. The user selects a preferred language.
4. The application creates a system instruction based on the selected options.
5. The question is sent to the Gemini 2.5 Flash model.
6. The generated response is displayed through the Gradio interface.

## 🔮 Future Enhancements

- Conversation history and memory
- Voice input and output
- Additional languages
- Chat-style interface
- File upload and document-based question answering
- Improved error handling and response customization

## 👨‍💻 Developer

**Chinmay Choudhari**

Computer Science Engineering Student | AI & Web Development Enthusiast

## 📜 License

This project is developed for learning, experimentation, and educational purposes.
