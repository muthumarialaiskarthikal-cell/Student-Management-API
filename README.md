
# Student Management REST API

## Project Description
This project is a Student Management REST API developed using Python Flask and SQLite.

It helps users to manage student details through API operations.

## Technologies Used
- Python
- Flask
- SQLite
- REST API

## Features
- Add Student
- View All Students
- View Student by ID
- Update Student Details
- Delete Student
- Input Validation
- SQLite Database

## Project Structure
Student-Management-API/
- app.py
- database.py
- requirements.txt
- README.md

## Installation

1. Clone the repository.

2. Install the required packages:

   pip install -r requirements.txt

3. Run the application:

   python app.py

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Home |
| POST | /students | Add Student |
| GET | /students | View Students |
| GET | /students/1 | View Student |
| PUT | /students/1 | Update Student |
| DELETE | /students/1 | Delete Student |

## Sample JSON Input

{
  "name": "Karthika",
  "department": "CSE",
  "mark": 85
}

## Database
SQLite is used to store student details.

## Author
Karthika

## Conclusion
This project demonstrates how to develop a REST API using Python Flask and SQLite.
