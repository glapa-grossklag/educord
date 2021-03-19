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
    notes: [Note]
    created_at: datetime

    def __init__(self, title: str):
        self.title = title
        self.notes = []
        self.datetime = datetime.now()

    def __len__(self):
        return len(self.notes)

    def __dict__(self):
        notebook = {self.title: {}}
        for note in self.notes:
            notebook[self.title][note.title] = note.content

    def add(self, note: Note):
        """
        Add a new note to the notebook
        """
        self.notes.append(note)

    def remove(self, note: Note):
        """
        Remove a note from the notebook
        """
        if note in self.notes:
            self.notes.remove(note)
        else:
            raise ValueError("Note is not in notebook")
