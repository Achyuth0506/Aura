# backend/core/profile.py

class UserProfile:
    """
    Stores inferred long-term user information.
    """

    def __init__(self):
        self.goals = set()
        self.challenges = set()
        self.preferences = {}

    def update_goal(self, goal: str):
        self.goals.add(goal)

    def update_challenge(self, challenge: str):
        self.challenges.add(challenge)

    def update_preference(self, key: str, value: str):
        self.preferences[key] = value

    def summary(self) -> str:
        parts = []

        if self.goals:
            parts.append("User goals: " + ", ".join(self.goals))

        if self.challenges:
            parts.append("User challenges: " + ", ".join(self.challenges))

        if self.preferences:
            pref_text = ", ".join(
                f"{k}={v}" for k, v in self.preferences.items()
            )
            parts.append("User preferences: " + pref_text)

        if not parts:
            return "No long-term profile established yet."

        return "\n".join(parts)

