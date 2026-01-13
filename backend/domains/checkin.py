from datetime import date

class DailyCheckIn:
    def __init__(self):
        self.entries = {}

    def log(self, mood: str, energy: str):
        today = date.today().isoformat()
        self.entries[today] = {
            "mood": mood,
            "energy": energy
        }

    def summary(self):
        if not self.entries:
            return "No daily check-ins yet."
        latest = sorted(self.entries.keys())[-1]
        e = self.entries[latest]
        return f"Latest check-in ({latest}): mood={e['mood']}, energy={e['energy']}"

