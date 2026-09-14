# KAI — Voice Assistant 🤖

**KAI** is a modular Python voice assistant designed to interact with the user through voice commands.

It can recognize spoken commands, open websites, launch Windows applications, play music, and use **Google Gemini AI** to answer questions and handle commands that are not built into the command system.

The project is designed with a modular architecture so that new features can be added without making the main program unnecessarily large.

---

## ✨ Features

* 🎙️ Voice command recognition
* 🗣️ Text-to-speech responses
* 🌐 Website and web-service control
* 🎵 Music playback
* 🖥️ Windows application launching
* 🤖 Gemini AI integration
* 🧩 Modular command architecture
* 🔀 Automatic command routing
* 💬 Natural AI responses
* ⚡ Simple and lightweight Python structure

---

## 🏗️ Project Structure

```text
KAI/
│
├── main.py
├── commands.py
├── responses.py
│
├── modules/
│   ├── __init__.py
│   ├── website_module.py
│   ├── music_module.py
│   ├── system_module.py
│   └── ai_module.py
│
└── requirements.txt
```

---

## 🔄 How KAI Works

KAI uses a simple command-routing architecture:

```text
                  🎙️ User Voice
                       │
                       ▼
                    main.py
                       │
                       ▼
                  commands.py
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
      Website        Music        System
       Module        Module        Module
          │            │            │
          └────────────┼────────────┘
                       │
                       ▼
                   AI Module
                       │
                       ▼
                 Google Gemini
```

The main program handles the voice interaction, while `commands.py` determines which module should process the command.

---

## 🧩 Modules

### `main.py`

The main entry point of KAI.

It handles:

* Microphone input
* Speech recognition
* Wake word detection
* Text-to-speech
* Command input
* Program loop

---

### `commands.py`

Acts as the command router.

It determines whether a command should be handled by:

* Website module
* Music module
* System module
* Gemini AI module

---

### `website_module.py`

Handles website-related commands.

Example:

```text
KAI, open Google
KAI, open YouTube
KAI, open Gmail
```

---

### `music_module.py`

Handles music playback.

Example:

```text
KAI, play Skyfall
KAI, play Wolf
KAI, play March
```

---

### `system_module.py`

Handles Windows system commands.

Example:

```text
KAI, launch Notepad
KAI, launch Calculator
KAI, launch Command Prompt
KAI, launch File Explorer
```

---

### `ai_module.py`

Handles commands that are not recognized by the built-in command system.

KAI sends the user's request to **Google Gemini** and speaks the generated response.

Example:

```text
KAI, what is artificial intelligence?
```

Gemini generates the response and KAI speaks it aloud.

---

## 🛠️ Requirements

* Python 3.x
* Windows
* Working microphone
* Internet connection
* Google Gemini API key

Python packages used by the project:

```text
SpeechRecognition
PyAudio
pyttsx3
google-genai
```

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/KAI.git
```

Enter the project directory:

```bash
cd KAI
```

---

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Gemini API Key

KAI uses Google Gemini for AI-powered responses.

Create a Gemini API key and add it to:

```text
modules/ai_module.py
```

For example:

```python
from google import genai

API_KEY = "YOUR_GEMINI_API_KEY"

client = genai.Client(
    api_key=API_KEY
)
```

## ▶️ Running KAI

Activate your virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

Then run:

```bash
python main.py
```

KAI will initialize and begin listening for the wake word.

Example:

```text
Initializing KAI.

Listening...
```

Say:

```text
KAI
```

and then give a command.

---

## 🎤 Example Commands

### Websites

```text
KAI, open Google
KAI, open YouTube
KAI, open Gmail
```

### Music

```text
KAI, play Skyfall
KAI, play Wolf
```

### Windows

```text
KAI, launch Notepad
KAI, launch Calculator
KAI, launch Command Prompt
```

### AI

```text
KAI, explain machine learning
KAI, what is Python?
KAI, tell me a joke
```

---

## 🧠 Why Modular?

Instead of putting every command inside one large Python file, KAI separates functionality into independent modules.

For example:

```text
Website commands
       ↓
website_module.py

Music commands
       ↓
music_module.py

System commands
       ↓
system_module.py

AI commands
       ↓
ai_module.py
```

This makes the project easier to:

* Maintain
* Debug
* Understand
* Extend
* Modify

New functionality can be added as a separate module without heavily changing the core application.

---

## 🚀 Future Improvements

Planned ideas for future versions:

* 🔊 Better voice interaction
* 🧠 Improved conversation memory
* 🪟 Graphical user interface
* 🌦️ Weather information
* 📰 News updates
* 📅 Reminders and scheduling
* 📁 File and folder automation
* 💻 More Windows system controls
* 🔌 Additional API integrations
* 🗣️ Improved natural-language command detection

---

## 📚 Technologies Used

| Technology        | Purpose                       |
| ----------------- | ----------------------------- |
| Python            | Core programming language     |
| SpeechRecognition | Speech-to-text                |
| PyAudio           | Microphone input              |
| pyttsx3           | Text-to-speech                |
| Google Gemini API | AI responses                  |
| Webbrowser        | Website control               |
| Subprocess        | Windows application launching |

---

## 📄 License

This project is open source and available for learning, experimentation, and personal use.

---

## 👨‍💻 Author

**Your Name**

Built with Python and Google Gemini.

---

⭐ If you find this project interesting, consider giving the repository a star!
