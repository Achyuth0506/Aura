class ConversationMemory:
    """
    Summarized short-term memory.
    Stores distilled understanding, not raw logs.
    """

    def __init__(self):
        self.summary = ""

    def update(self, user_input: str, assistant_response: str):
        """
        Update memory with a compressed representation.
        """
        new_insight = f"""
User expressed: {user_input}
Aura responded with guidance.
"""

        self.summary = (self.summary + "\n" + new_insight).strip()

    def get_summary(self) -> str:
        if not self.summary:
            return "No prior user context."
        return self.summary

