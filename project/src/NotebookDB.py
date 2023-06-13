import sqlite3
from datetime import datetime

import resources.constants as const


NOTES_DATABASE_PATH = "resources/notebook.db"
CREATE_NOTES_TABLE_SQL = """
    CREATE TABLE IF NOT EXISTS Notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        scheduled BOOLEAN,
        scheduled_at TEXT,
        content TEXT,
        tags TEXT,
        created_at TEXT
    )
"""
OVERRITE_NOTES_TABLE_ON_SAVE_SQL = """
    DROP TABLE IF EXISTS Notes;
"""
SELECT_ALL_NOTES_SQL = """
    SELECT * FROM Notes
"""
INSERT_NOTE_SQL = """
    INSERT INTO Notes (title, scheduled, scheduled_at, content, tags, created_at)
    VALUES (?, ?, ?, ?, ?, ?)
"""


def load_notes(app):
    database = sqlite3.connect(NOTES_DATABASE_PATH)
    cursor = database.cursor()
    cursor.execute(CREATE_NOTES_TABLE_SQL)
    cursor.execute(SELECT_ALL_NOTES_SQL)
    for note in cursor.fetchall():
        id, title, scheduled, scheduled_at, content, tags, created_at = note
        scheduled_at = datetime.strptime(scheduled_at, const.DEFAULT_DATETIME_FORMAT)
        created_at = datetime.strptime(created_at, const.DEFAULT_DATETIME_FORMAT)
        app.note_count = id
        note = app.notebook.add(
            title=title,
            scheduled=scheduled,
            scheduled_at=scheduled_at,
            content=content,
            tags=tags.split(","),
            created_at=created_at,
        )
    database.close()


def save_notes(app):
    database = sqlite3.connect(NOTES_DATABASE_PATH)
    cursor = database.cursor()
    cursor.execute(OVERRITE_NOTES_TABLE_ON_SAVE_SQL)
    cursor.execute(CREATE_NOTES_TABLE_SQL)
    for note in app.notebook:
        cursor.execute(
            INSERT_NOTE_SQL,
            (
                note.title,
                note.scheduled,
                note.scheduled_at.strftime(const.DEFAULT_DATETIME_FORMAT),
                note.content,
                ",".join(note.tags),
                note.created_at.strftime(const.DEFAULT_DATETIME_FORMAT),
            ),
        )
    database.commit()
    database.close()
