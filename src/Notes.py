from discord.ext import commands
from discord.ext.commands import Context


class Note:

    def __init__(self, name):
        self.name = name
        self.notes = {}
        self.numNotes = 0

    def add_note(self, title, content):
        self.notes[title] = content

    def del_note(self, key):
        if key in self.notes:
            del self.notes[key]
