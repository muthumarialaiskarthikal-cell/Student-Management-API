
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Database connection
def get_db():
    conn = sqlite3.connect("students.db")
    conn.row_factory = sqlite3.Row
    return conn

# Create database table
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

# Home API
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Student Management API is running"
    })

# Add student
@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()

    if not data or not all(key in data for key in ["name", "department", "mark"]):
        return jsonify({"error": "Missing student details"}), 400

    if not isinstance(data["mark"], int) or not 0 <= data["mark"] <= 100:
        return jsonify({"error": "Mark must be between 0 and 100"}), 400

    conn = get_db()
    conn.execute(
        "INSERT INTO students (name, department, mark) VALUES (?, ?, ?)",
        (data["name"], data["department"], data["mark"])
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Student added successfully"}), 201

# View all students
@app.route("/students", methods=["GET"])
def view_students():
    conn = get_db()
    students = conn.execute("SELECT * FROM students").fetchall()
    conn.close()

    return jsonify([dict(student) for student in students])

# View one student
@app.route("/students/<int:id>", methods=["GET"])
def get_student(id):
    conn = get_db()
    student = conn.execute(
        "SELECT * FROM students WHERE id = ?", (id,)
    ).fetchone()
    conn.close()

    if student is None:
        return jsonify({"error": "Student not found"}), 404

    return jsonify(dict(student))

# Update student
@app.route("/students/<int:id>", methods=["PUT"])
def update_student(id):
    data = request.get_json()

    if not data or not all(key in data for key in ["name", "department", "mark"]):
        return jsonify({"error": "Missing student details"}), 400

    if not isinstance(data["mark"], int) or not 0 <= data["mark"] <= 100:
        return jsonify({"error": "Invalid mark"}), 400

    conn = get_db()
    result = conn.execute(
        "UPDATE students SET name=?, department=?, mark=? WHERE id=?",
        (data["name"], data["department"], data["mark"], id)
    )
    conn.commit()
    conn.close()

    if result.rowcount == 0:
        return jsonify({"error": "Student not found"}), 404

    return jsonify({"message": "Student updated successfully"})

# Delete student
@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    conn = get_db()
    result = conn.execute(
        "DELETE FROM students WHERE id=?", (id,)
    )
    conn.commit()
    conn.close()

    if result.rowcount == 0:
        return jsonify({"error": "Student not found"}), 404

    return jsonify({"message": "Student deleted successfully"})

if __name__ == "__main__":
    create_table()
    app.run(host="0.0.0.0", port=5000, debug=True)
  
