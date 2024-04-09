import sqlite3

conn = sqlite3.connect('addresses.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS addresses
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              street TEXT,
              city TEXT,
              state TEXT,
              country TEXT,
              latitude REAL,
              longitude REAL)''')
conn.commit()