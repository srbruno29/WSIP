import sqlite3

conn = sqlite3.connect("games.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS games (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    genre TEXT NOT NULL,
    status TEXT NOT NULL,
    cover_url TEXT,
    release_date TEXT,
    rating REAL
)
""")

conn.commit()
conn.close()

print("Banco criado/atualizado (sem plataforma)")