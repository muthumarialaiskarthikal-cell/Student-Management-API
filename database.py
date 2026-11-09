
import sqlite3

# Connect to database
def get_db():
    conn = sqlite3.connect("students.db")
    conn.row_factory = sqlite3.Row
    return conn

# Create student table
def create_table():
    conn = get_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            mark INTEGER NOT NULL
        )
    """)

    conn.commit()
    conn.close()

    print("Database and table created successfully!")

if __name__ == "__main__":
    create_table()
  
