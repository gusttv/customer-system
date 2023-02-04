import sqlite3

def create_database():
    conn = sqlite3.connect("customers.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT
    )
    """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
