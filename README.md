# 🎯 LIMMA Software Projects

## A Collection of Voice-Powered Python Applications

<div align="center">
  
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![LIMMA](https://img.shields.io/badge/LIMMA-Framework-green)
![License](https://img.shields.io/badge/License-MIT-orange)
![GitHub](https://img.shields.io/github/stars/firoziya/limma?style=social)

<!-- show the limma package download badge -->
![LIMMA Downloads](https://img.shields.io/pypi/dm/limma?color=blue&label=limma%20downloads)

### *Speak. Command. Create.*

</div>

---

## 📦 What is this?

This repository contains **5 easy-to-use voice-controlled applications** built with the LIMMA framework. Each app lets you control things with your voice instead of typing.

---

## 🚀 Quick Start in 3 Steps

```bash
# 1. Clone and enter
git clone https://github.com/firoziya/limma-projects-software.git
cd limma-projects-software

# 2. Setup
python setup.py

# 3. Run any app
python run.py
```

---

## 📱 The 5 Apps

| # | App | What it does | Run command |
|---|-----|--------------|-------------|
| 1 | **Voice Assistant** | AI friend who answers questions | `python assistant.py` |
| 2 | **Voice Editor** | Write documents by speaking | `python editor.py` |
| 3 | **Voice Notes** | Save and manage voice notes | `python notes.py` |
| 4 | **Translator** | Translate between 15 languages | `python translator.py` |
| 5 | **Chat App** | Use LLM Chat App | `python chat.py` |

---

## 🎤 App Details

### 1. 🤖 Smart Voice Assistant
**File:** `assistant.py`

Your personal AI assistant. Ask anything!

```bash
python assistant.py
```

**What you can say:**
- "What time is it?"
- "Search for Python tutorials"
- "Note down buy milk"
- "Tell me a joke"
- "Calculate 25 * 4"
- "Goodbye" (to exit)

---

### 2. 📝 Voice Text Editor
**File:** `editor.py`

Write documents without typing!

```bash
python editor.py
```

**Voice commands:**
- "New file"
- "Open mydoc.txt"
- "Add Hello world"
- "Read content"
- "Save"
- "Exit"

---

### 3. 📒 Voice Notes App
**File:** `notes.py`

Save and organize voice notes.

```bash
python notes.py
```

**Commands:**
- "Create note"
- "Search notes"
- "Read my notes"
- "Delete note"
- "Show summary"
- "Exit"

---

### 4. 🌍 AI Translator
**File:** `translator.py`

Translate between 15 languages.

```bash
python translator.py
```

**Menu options:**
1. Text Translation
2. Voice Translation  
3. Conversation Mode
4. Batch Translation
5. View History
6. Exit

**Supported languages:** Spanish, French, German, Italian, Portuguese, Russian, Japanese, Chinese, Arabic, Hindi, and more!

---

### 5. 🏠 IoT Control System
**File:** `iot.py`

Control smart devices with voice.

```bash
python iot.py
```

**Commands:**
- "Add device"
- "Show devices"
- "Turn on light"
- "Create schedule"
- "Show status"

---

## ⚙️ Setup Guide

### What you need:
- Python 3.8 or higher
- Microphone (built-in is fine)
- Speakers/headphones
- Internet (for AI features)

### Step-by-step:

```bash
# 1. Get the code
git clone https://github.com/firoziya/limma-projects-software.git
cd limma-projects-software

# 2. Install requirements
pip install -r requirements.txt

# 3. Test your microphone
python test_mic.py

# 4. Run any app
python assistant.py  # or editor.py, notes.py, etc.
```

---

## 🔑 API Keys (Optional)

Some apps need free API keys for AI features:

### For Voice Assistant (Gemini AI)
1. Go to [makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)
2. Sign in with Google
3. Click "Create API Key"
4. Copy the key

### For Translator (Groq)
1. Go to [console.groq.com](https://console.groq.com)
2. Sign up free
3. Get API key

### Add keys to `.env` file:
```bash
# Create .env file
echo "GEMINI_API_KEY=your-key-here" > .env
echo "GROQ_API_KEY=your-key-here" >> .env
```

---

## 🎮 How to Use Any App

1. **Run the app** (using commands above)
2. **Wait for voice prompt** ("Listening..." or voice greeting)
3. **Speak clearly** into your microphone
4. **See the result** on screen and hear voice response
5. **Say "exit" or "goodbye"** to quit

---

## ❓ Common Issues & Fixes

| Problem | Solution |
|---------|----------|
| **Microphone not working** | Check if mic is plugged in. Run `python test_mic.py` |
| **No voice output** | Check speakers, turn up volume |
| **App not starting** | Make sure Python 3.8+ is installed |
| **API errors** | Add your API keys to `.env` file |
| **Slow response** | Check internet connection |

---

## 📁 Project Files

```
limma-projects-software/
├── assistant.py          # Voice Assistant app
├── editor.py             # Voice Text Editor
├── notes.py              # Voice Notes app
├── translator.py         # AI Translator
├── iot.py                # IoT Control
├── setup.py              # Quick setup script
├── run.py                # Launcher menu
├── test_mic.py           # Test microphone
├── requirements.txt      # All dependencies
├── .env.example          # API keys template
└── README.md             # This file
```

---

## 🚦 Quick Commands Cheat Sheet

### For ALL apps:
- Say **"help"** - Show available commands
- Say **"exit"** or **"goodbye"** - Quit app
- Press **Ctrl+C** - Force quit

### App-specific:

| App | Main Commands |
|-----|--------------|
| **assistant.py** | time, date, search, note, joke, calculate |
| **editor.py** | new, open, save, add, read, delete |
| **notes.py** | create, search, read, delete, summary |
| **translator.py** | (menu-driven, numbers 1-6) |
| **iot.py** | add, show, on, off, schedule |

---

## 🤝 Want to Contribute?

Simple steps:

1. Fork this repo
2. Make your changes
3. Test it works
4. Send a pull request

**Ideas for contribution:**
- Add more voice commands
- Fix bugs
- Improve voice recognition
- Add new languages
- Create better documentation

---

## 📞 Need Help?

- **GitHub Issues**: [Click here](https://github.com/firoziya/limma-projects-software/issues)
- **Email**: firoziya@limma.live
- **Website**: [limma.live](https://limma.live)

---

## 📄 License

Free to use, modify, and share. MIT License.

---

<div align="center">
  
### ⭐ Star this repo if you like it!

**Made with ❤️ by Firoziya**

[GitHub](https://github.com/firoziya) • [Website](https://limma.live)

</div>

---

*Happy voice coding! 🎤✨*
