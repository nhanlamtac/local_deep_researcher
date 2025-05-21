import sqlite3
import os
# 1. connect (this will create papers.db if it doesn't exist)
conn = sqlite3.connect('papers.db')
c = conn.cursor()

# 2. create table (ignore error if it already exists)


c.execute("""
CREATE TABLE IF NOT EXISTS papers (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    title    TEXT    NOT NULL,
    abstract TEXT,
    source TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# # 3. insert one paper
# title = "A Survey on Event-Based Vision"
# abstract = """Event-based cameras report changes in brightness asynchronously...
# ...
# which can improve latency and dynamic range."""
# c.execute("INSERT INTO papers (title, abstract) VALUES (?, ?)", (title, abstract))

c.execute("SELECT id, title, abstract, source, created_at FROM papers")
for row in c.fetchall():
    print(row)
# 4. commit & close
conn.commit()
conn.close()