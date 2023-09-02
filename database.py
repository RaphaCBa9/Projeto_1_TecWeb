import sqlite3
from dataclasses import dataclass


@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ""


class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(f"{db_name}.db")
        self.create_table()

    def get(self, note_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, title, content FROM note WHERE id = ?", (note_id,))
        row = cursor.fetchone()
        note = Note(id=row[0], title=row[1], content=row[2])
        return note

    def create_table(self):
        cursor = self.conn.cursor()
        comando = "CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, title TEXT NOT NULL, content TEXT NOT NULL)"
        cursor.execute(comando)

    def add(self, note):
        cursor = self.conn.cursor()
        comando = f'INSERT INTO notes (title, content) VALUES ("{note.title}", "{note.content}")'
        cursor.execute(comando)
        self.conn.commit()

    def get_all(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, title, content FROM notes")
        notes = []
        for i in cursor:
            note = Note(id=i[0], title=i[1], content=i[2])
            notes.append(note)
        return notes

    def update(self, entry):
        cursor = self.conn.cursor()
        comando = f'UPDATE notes SET title="{entry.title}", content="{entry.content}" WHERE id={entry.id}'
        cursor.execute(comando)
        self.conn.commit()

    def delete(self, entry_id):
        cursor = self.conn.cursor()
        comando = f"DELETE FROM notes WHERE id={entry_id}"
        cursor.execute(comando)
        self.conn.commit()
