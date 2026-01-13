# backend/core/plans.py

class TaskPlan:
    def __init__(self, title: str, steps: list[str]):
        self.title = title
        self.steps = steps
        self.current_step = 0

    def next_step(self):
        if self.current_step < len(self.steps):
            step = self.steps[self.current_step]
            self.current_step += 1
            return step
        return None

    def is_complete(self):
        return self.current_step >= len(self.steps)

    def display(self) -> str:
        output = [f"Plan: {self.title}"]
        for i, step in enumerate(self.steps, start=1):
            marker = "✅" if i <= self.current_step else "⬜"
            output.append(f"{marker} {i}. {step}")
        return "\n".join(output)


class PlanStore:
    def __init__(self):
        self.plans = []

    def add_plan(self, plan: TaskPlan):
        self.plans.append(plan)

    def latest_plan(self):
        if not self.plans:
            return None
        return self.plans[-1]

