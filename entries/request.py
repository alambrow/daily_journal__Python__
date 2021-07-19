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