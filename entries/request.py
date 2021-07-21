import sqlite3
import json
from models import Entry, Mood

def get_all_entries():
    with sqlite3.connect("./dailyjournal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.title,
            a.entry,
            a.timestamp,
            a.moodId,
            b.id mood_id,
            b.mood mood
        FROM Entries a
        JOIN Moods b
            ON b.id = a.moodId;
        """)

        entries = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            entry = Entry(row['id'], row['title'], row['entry'], row['timestamp'], row['moodId'])
            mood = Mood(row['id'], row['mood'])
            entry.mood = mood.__dict__
            entries.append(entry.__dict__)
    
    return json.dumps(entries)

def get_entry_by_id(id):
    with sqlite3.connect("./dailyjournal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.title,
            a.entry,
            a.timestamp,
            a.moodId
        FROM entries a
        WHERE a.id = ?
        """, (id, ))

        row = db_cursor.fetchone()
        entry = Entry(row['id'], row['title'], row['entry'], row['timestamp'], row['moodId'])
        return json.dumps(entry.__dict__)

def delete_entry(id):
    with sqlite3.connect("./dailyjournal.db") as taco:
        database_cursor = taco.cursor()

        database_cursor.execute("""
        DELETE FROM entries
        WHERE id = ?
        """, (id, ))

def find_entry_by_keyword(searchTerm):
    with sqlite3.connect("./dailyjournal.db") as conn:
        
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute(f"""
        SELECT
            a.id,
            a.title,
            a.entry,
            a.timestamp,
            a.moodId
        FROM entries a
        WHERE entry LIKE "%{searchTerm}%";
        """)
        entries = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            entry = Entry(row['id'], row['title'], row['entry'], row['timestamp'], row['moodId'])
            entries.append(entry.__dict__)
    
    return json.dumps(entries)

def create_journal_entry(new_entry):
    with sqlite3.connect("./dailyjournal.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.excute("""
        INSERT INTO Entries
            ( title, entry, timestamp, moodId)
        VALUES
            ( ?, ?, ?, ?);
        """, (new_entry['title'], new_entry['entry'], new_entry['timestamp'], new_entry['moodId']))
        new_id = db_cursor.lastrowid
        new_entry['id'] = new_id
    return json.dumps(new_entry)