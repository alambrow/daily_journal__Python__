import sqlite3
import json
from models import Entry

def get_all_entries():
    with sqlite3.connect("./dailyjournal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.title,
            a.entry,
            a.timestamp
        FROM entries a
        """)

        entries = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            entry = Entry(row['id'], row['title'], row['entry'], row['timestamp'])
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
            a.timestamp
        FROM entries a
        WHERE a.id = ?
        """, (id, ))

        row = db_cursor.fetchone()
        entry = Entry(row['id'], row['title'], row['entry'], row['timestamp'])
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
        searchT = searchTerm
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            a.id,
            a.title,
            a.entry,
            a.timestamp
        FROM entries a
        WHERE entry LIKE '%{searchT}%';
        """)
        entries = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            entry = Entry(row['id'], row['title'], row['entry'], row['timestamp'])
            entries.append(entry.__dict__)
    
    return json.dumps(entries)