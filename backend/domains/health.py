class HealthTracker:
    def __init__(self):
        self.logs = []

    def log_activity(self, text: str):
        self.logs.append(text)

    def summary(self) -> str:
        if not self.logs:
            return "No health activity logged yet."
        return "Recent health activity:\n" + "\n".join(self.logs[-5:])

