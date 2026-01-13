from backend.core.plans import TaskPlan

def generate_plan(task_description: str) -> TaskPlan:
    steps = [
        "Clarify the requirements and expectations",
        "Gather necessary information or materials",
        "Break the work into smaller sections",
        "Complete each section one by one",
        "Review and finalize the result",
    ]

    return TaskPlan(
        title=task_description,
        steps=steps,
    )

