class Note:

    def __init__(self, name):
        self.name = name
        self.notes = {}

    def __len__(self):
        return len(self.notes)

    def add_note(self, title, content):
        self.notes[title] = content

    def del_note(self, key):
        if key in self.notes:
            del self.notes[key]
