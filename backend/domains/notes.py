class NotesVault:
    def __init__(self):
        self.notes = []

    def add_note(self, note: str):
        self.notes.append(note)

    def summary(self) -> str:
        if not self.notes:
            return "No notes saved."
        return "Recent notes:\n" + "\n".join(self.notes[-5:])

