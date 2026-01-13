def detect_personal_intent(text: str):
    text = text.lower()

    if text.startswith("log ") or "walked" in text or "worked out" in text:
        return "health"

    if text.startswith("goal "):
        return "goal"

    if text.startswith("note "):
        return "note"

    if text.startswith("remind"):
        return "calendar"

    if "check in" in text:
        return "checkin"

    if "daily summary" in text:
        return "daily_summary"

    if "weekly summary" in text:
        return "weekly_summary"

    if "show summary" in text or "summary" in text:
        return "summary"

    return "general"


def extract_goal_or_challenge(text: str):
    t = text.lower()
    if "want to" in t or t.startswith("goal"):
        return "goal", text
    if "struggle" in t or "distracted" in t:
        return "challenge", text
    return None, None


def parse_reminder(text: str):
    text = text.lower()
    if "at" in text:
        parts = text.split("at")
        return parts[0].replace("remind me to", "").strip(), parts[1].strip()
    return None, None

