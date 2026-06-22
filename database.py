import sqlite3

conn = sqlite3.connect(
    "safetyeye.db"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS alerts(
id INTEGER PRIMARY KEY AUTOINCREMENT,
time TEXT,
alert TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS occupancy(
id INTEGER PRIMARY KEY AUTOINCREMENT,
time TEXT,
count INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS login_history(
id INTEGER PRIMARY KEY AUTOINCREMENT,
time TEXT,
username TEXT
)
""")

conn.commit()

conn.close()

print("Database Created")