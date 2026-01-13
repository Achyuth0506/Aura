class GoalManager:
    def __init__(self):
        self.goals = []

    def add_goal(self, goal: str):
        self.goals.append(goal)

    def summary(self) -> str:
        if not self.goals:
            return "No active goals."
        return "Active goals:\n" + "\n".join(self.goals)

