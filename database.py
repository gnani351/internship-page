import sqlite3

conn = sqlite3.connect("internship.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS registrations(
id INTEGER PRIMARY KEY AUTOINCREMENT,
fullname TEXT,
email TEXT,
phone TEXT,
dob TEXT,
gender TEXT,
college TEXT,
degree TEXT,
branch TEXT,
year TEXT,
domain TEXT,
resume TEXT
)
""")

conn.commit()
conn.close()

print("Database Created")