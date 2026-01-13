# 🧠 Aura — Personal AI Life Agent

Aura is a personal AI life agent designed to help users track health activities, manage goals, store notes, set reminders, and reflect through daily and weekly summaries — all in one place.

Unlike typical chatbots, Aura combines deterministic domain logic with selective LLM reasoning, ensuring trustworthy behavior, persistent memory, and non-intrusive assistance suitable for real-world personal use.

---

## ✨ Key Features

### 🏃 Health & Activity Tracking
- Log daily activities (e.g., walks, workouts)
- View recent health summaries
- Supports habit reflection (non-medical, safe by design)

### 🎯 Goal Management
- Add and track personal goals
- Goals are retained across sessions
- Enables goal-aligned nudges (never forced)

### 📝 Notes
- Store free-form personal notes
- Retrieve recent notes instantly
- Notes persist across restarts

### 📅 Reminders & Events
- Add simple time-based reminders
- View upcoming events
- No automatic scheduling without user intent

### 🧠 Daily Check-ins
- Log mood and energy levels
- Track well-being over time
- Used only for reflection, not diagnosis

### 📊 Daily & Weekly Summaries
- Generate summaries of tracked data
- Encourage reflection and planning
- Lightweight and user-controlled

### 🔐 Persistent Memory
- All user data is saved locally (JSON-based persistence)
- Aura remembers state across app restarts
- No external databases required

---

## 🏗️ Architecture Overview
```
User
↓
Streamlit UI
↓
App Orchestrator (app.py)
↓
Intent Router
↓
┌──────────┬──────────┬──────────┬──────────┐
│ Health │ Goals │ Notes │ Calendar │
│ Tracker │ Manager │ Vault │ Manager │
└──────────┴──────────┴──────────┴──────────┘
↓
Memory & Profile
↓
LLM (used only when reasoning is required)

```


## 🛠️ Tech Stack

- Python 3.12
- Streamlit
- OpenAI API
- JSON-based local persistence
- Modular backend architecture

---

## 🚀 Run Locally

```bash
git clone https://github.com/Achyuth0506/aura.git
cd aura
pip install -r requirements.txt
export OPENAI_API_KEY="sk-..."
streamlit run app.py
☁️ Deployment (Streamlit Cloud)
Push repository to GitHub

Go to https://share.streamlit.io

Create new app:

Repository: Achyuth0506/aura

Branch: main

File: app.py

Add secret:

toml
Copy code
OPENAI_API_KEY = "sk-..."
Deploy
```

## 🔐 Security & Privacy
API keys are never hardcoded

Local dev uses environment variables

Cloud deployment uses Streamlit Secrets

Personal data stored locally in JSON

No external databases

## 📈 Future Improvements
Background reminders

Multi-user authentication

Calendar API integration

Habit streak analytics

Vector-based long-term memory
