def daily_summary(state):
    return (
        "🗓 Daily Summary\n"
        f"- Health logs: {len(state.get('health', []))}\n"
        f"- Notes: {len(state.get('notes', []))}\n"
        f"- Goals: {len(state.get('goals', []))}"
    )

def weekly_summary(state):
    return (
        "📊 Weekly Summary\n"
        "You’ve been consistently tracking your life.\n"
        "Would you like to review patterns or set priorities for next week?"
    )

