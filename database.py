import sqlite3

conn = sqlite3.connect("db.sqlite")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS uploads (
    channel TEXT,
    filename TEXT
)
""")

def is_uploaded(channel, filename):
    c.execute("SELECT * FROM uploads WHERE channel=? AND filename=?", (channel, filename))
    return c.fetchone() is not None

def mark_uploaded(channel, filename):
    c.execute("INSERT INTO uploads VALUES (?, ?)", (channel, filename))
    conn.commit()