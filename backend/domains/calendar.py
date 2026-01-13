from datetime import datetime

class CalendarManager:
    def __init__(self):
        self.events = []

    def add_event(self, description: str, remind_at: str = None):
        self.events.append({
            "description": description,
            "remind_at": remind_at
        })

    def due_events(self, now: datetime):
        due = []
        for e in self.events:
            if e["remind_at"]:
                try:
                    t = datetime.fromisoformat(e["remind_at"])
                    if t <= now:
                        due.append(e)
                except ValueError:
                    pass
        return due

    def summary(self):
        if not self.events:
            return "No upcoming events."
        return "Upcoming events:\n" + "\n".join(
            f"- {e['description']} @ {e['remind_at']}"
            for e in self.events
        )

