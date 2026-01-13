def build_context(memory_summary: str) -> str:
    return f"""
You have the following understanding of the user so far:

{memory_summary}

Based on this, you should:
- Respond to the user's current input
- If appropriate, suggest one helpful next action
- Do NOT overwhelm the user
"""

