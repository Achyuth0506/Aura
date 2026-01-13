import streamlit as st
from datetime import datetime

from backend.core.llm import generate_response
from backend.core.memory import ConversationMemory
from backend.core.profile import UserProfile
from backend.core.router import (
    detect_personal_intent,
    extract_goal_or_challenge,
    parse_reminder,
)
from backend.domains.health import HealthTracker
from backend.domains.goals import GoalManager
from backend.domains.notes import NotesVault
from backend.domains.calendar import CalendarManager
from backend.domains.checkin import DailyCheckIn
from backend.domains.summaries import daily_summary, weekly_summary
from backend.utils.persistence import save_state, load_state

st.set_page_config(page_title="Aura", page_icon="🧠")
st.title("🧠 Aura — Personal Life Agent")

# ------------------ Session Init ------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "memory" not in st.session_state:
    st.session_state.memory = ConversationMemory()

if "profile" not in st.session_state:
    st.session_state.profile = UserProfile()

if "health" not in st.session_state:
    st.session_state.health = HealthTracker()

if "goals" not in st.session_state:
    st.session_state.goals = GoalManager()

if "notes" not in st.session_state:
    st.session_state.notes = NotesVault()

if "calendar" not in st.session_state:
    st.session_state.calendar = CalendarManager()

if "checkin" not in st.session_state:
    st.session_state.checkin = DailyCheckIn()

# ------------------ Load State ------------------
saved = load_state()
if saved:
    st.session_state.health.logs = saved.get("health", [])
    st.session_state.goals.goals = saved.get("goals", [])
    st.session_state.notes.notes = saved.get("notes", [])
    st.session_state.calendar.events = saved.get("calendar", [])
    st.session_state.checkin.entries = saved.get("checkins", {})

# ------------------ Dashboard ------------------
with st.expander("📊 My Dashboard"):
    st.write(st.session_state.health.summary())
    st.write(st.session_state.goals.summary())
    st.write(st.session_state.notes.summary())
    st.write(st.session_state.calendar.summary())
    st.write(st.session_state.checkin.summary())

# ------------------ Chat ------------------
for m in st.session_state.messages:
    st.markdown(f"**{m['role'].title()}:** {m['content']}")

user_input = st.text_input("Talk to Aura")

if st.button("Send") and user_input:
    lower = user_input.lower()
    intent = detect_personal_intent(user_input)

    st.session_state.messages.append({"role": "user", "content": user_input})

    health = st.session_state.health
    goals = st.session_state.goals
    notes = st.session_state.notes
    calendar = st.session_state.calendar
    checkin = st.session_state.checkin
    memory = st.session_state.memory
    profile = st.session_state.profile

    kind, value = extract_goal_or_challenge(user_input)
    if kind == "goal":
        profile.update_goal(value)
    elif kind == "challenge":
        profile.update_challenge(value)

    desc, time_str = parse_reminder(lower)
    if desc and time_str:
        calendar.add_event(desc, datetime.now().date().isoformat() + "T" + time_str)
        response = f"⏰ Reminder set for {time_str}"

    elif intent == "health":
        health.log_activity(user_input)
        response = "✅ Health activity logged."

    elif intent == "goal":
        goals.add_goal(user_input)
        response = "🎯 Goal added."

    elif intent == "note":
        notes.add_note(user_input)
        response = "📝 Note saved."

    elif intent == "calendar":
        calendar.add_event(user_input)
        response = "📅 Event added."

    elif intent == "checkin":
        response = "How are you feeling today? (mood: good/ok/low, energy: high/medium/low)"

    elif "mood:" in lower and "energy:" in lower:
        mood = lower.split("mood:")[1].split()[0]
        energy = lower.split("energy:")[1].split()[0]
        checkin.log(mood, energy)
        response = "✅ Check-in saved."

    elif intent == "daily_summary":
        response = daily_summary(load_state())

    elif intent == "weekly_summary":
        response = weekly_summary(load_state())

    elif intent == "summary":
        response = (
            health.summary() + "\n\n" +
            goals.summary() + "\n\n" +
            notes.summary() + "\n\n" +
            calendar.summary()
        )

    else:
        response = generate_response(
            user_input,
            memory.get_summary() + "\n" + profile.summary()
        )

    memory.update(user_input, response)
    st.session_state.messages.append({"role": "assistant", "content": response})

    save_state({
        "health": health.logs,
        "goals": goals.goals,
        "notes": notes.notes,
        "calendar": calendar.events,
        "checkins": checkin.entries,
    })

    st.rerun()

