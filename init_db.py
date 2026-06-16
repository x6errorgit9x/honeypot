import sqlite3

conn = sqlite3.connect("attacks.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS attacks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ip TEXT,
    username TEXT,
    password TEXT,
    timestamp TEXT,
    technique TEXT,
    country TEXT,
    city TEXT
)
''')

conn.commit()
conn.close()
print("Database initialized.")
