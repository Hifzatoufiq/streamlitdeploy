import sqlite3

DB = "appraisal.db"

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        working_days INTEGER,
        present INTEGER,
        leave_days INTEGER,
        punctuality REAL,
        regularity REAL,
        performance REAL,
        total_score REAL,
        rating TEXT
    )
    """)
    conn.commit()
    conn.close()


def insert_employee(data):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""
    INSERT INTO employees
    (name, working_days, present, leave_days,
     punctuality, regularity, performance,
     total_score, rating)
    VALUES (?,?,?,?,?,?,?,?,?)
    """, data)
    conn.commit()
    conn.close()


def get_all():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT * FROM employees ORDER BY id DESC")
    rows = c.fetchall()
    conn.close()
    return rows
