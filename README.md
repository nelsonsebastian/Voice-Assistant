# Python Voice Assistant

A beginner-friendly voice assistant built in Python. Jarvis listens for a wake word, understands basic voice commands, and answers general questions using Google's Gemini AI, combining speech recognition, text-to-speech, and a large language model into a single assistant.

## Features

- Wake-word activation ("hello jarvis")
- Opens websites via voice command: Google, Facebook, YouTube, LinkedIn
- Plays songs from a custom music library
- Answers general questions using Google Gemini AI
- Speaks responses aloud using offline text-to-speech

## Tech Stack

- Python 3
- speech_recognition - converts speech to text
- pyttsx3 - offline text-to-speech
- google-genai - Google Gemini AI SDK
- PyAudio - microphone access
- webbrowser - built-in Python module for opening URLs

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

### 3. Install dependencies

All required packages are listed in requirements.txt.

```bash
pip install -r requirements.txt
```

Note (Windows only): This project uses pywin32 and comtypes, which are Windows-specific packages required by pyttsx3 for text-to-speech. If running on Mac or Linux, remove pywin32 and comtypes from requirements.txt before installing, since they will not install on those platforms.

### 4. Set your Gemini API key

Obtain a free API key from Google AI Studio (https://aistudio.google.com/apikey), then set it as an environment variable. Do not hardcode the key in the script.

Windows (PowerShell):

```powershell
setx GEMINI_API_KEY "your_key_here"
```

Restart the terminal after running this command.

Mac/Linux:

```bash
export GEMINI_API_KEY="your_key_here"
```

### 5. Add your own songs

Edit musicliberary.py and add entries in the following format:

```python
music={
    "song name" : "https://youtube-link-here"
}
```

### 6. Run Jarvis

```bash
python main.py
```

## Usage

1. Say "hello jarvis" to activate the assistant.
2. Jarvis responds with "how may I help you?"
3. Speak a command:
   - "open google" / "open youtube" / "open facebook" / "open linkedin"
   - "play [song name]" - plays a song from the music library
   - Any other input is forwarded to Gemini AI, which generates a spoken response

## Project Structure

```
Mega Project 1/
    main.py               Core program logic
    musicliberary.py       Song name to link dictionary
    requirements.txt       Python package dependencies
    .venv/                 Virtual environment (not committed to git)
    __pycache__/           Auto-generated Python cache (not committed to git)
```

## Security Note

Do not commit API keys to version control. If pushing this repository publicly, add a .gitignore file containing:

```
.venv/
__pycache__/
*.pyc
```

## License

This project is open source and available for learning purposes.
