from datetime import datetime

class Note:
    title: str
    content: str
    created_at: datetime

    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content
        self.created_at = datetime.now()

class Notebook:
    title: str
    notes: list[Note]
    created_at: datetime

    def __init__(self, title: str):
        self.title = title
        self.notes = []
        self.datetime = datetime.now()

    def __len__(self):
        return len(self.notes)

    """
    Add a new note to the notebook
    """
    def add(self, note: Note):
        self.notes.append(note)

    """
    Remove a note from the notebook
    """
    def remove(self, note: Note):
        if note in self.notes:
            self.notes.remove(note)
        else:
            raise ValueError("Note is not in notebook")
