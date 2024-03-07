import sqlite3
import os

FLAG = os.getenv("FLAG", "agrihack{4bd74919-9ade-4faa-aab5-b292f68f9cf4}")

conn = sqlite3.connect("database.db")
conn.execute("""CREATE TABLE community (
  code TEXT NOT NULL,
  name TEXT NOT NULL
);""")
conn.execute("""CREATE TABLE flag (
  flag TEXT NOT NULL
);""")
conn.execute(f"INSERT INTO flag VALUES (?)", (FLAG,))

countries = [
    ('CSI', 'Cyber Security IPB'),
    ('CP', 'Competitive Programming'),
    ('IPWC', 'IPB Web Development Comunity'),
    ('MAD', 'Mobile Apps Development'),
    ('DM', 'Data Mining'),
]
conn.executemany("INSERT INTO community VALUES (?, ?)", countries)

conn.commit()
conn.close()
