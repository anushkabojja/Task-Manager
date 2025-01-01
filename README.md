# Task-Manager
zensor project
Task Manager
Description
The Task Manager is a Python-based project designed to automatically generate and manage college timetables. It accounts for teachers, subjects, and specific scheduling rules to create an efficient, conflict-free schedule for the entire week. The tool aims to simplify the process of timetable creation while ensuring fair distribution of work among teachers.

Features
Dynamic Timetable Generation: Automatically generates a timetable based on the number of teachers, their subjects, and the classes.
Customizable Scheduling:
Includes practical sessions, lectures, and meetings.
Guarantees one practical session per day and proper lunch breaks.
Allocates special slots for teacher and student meetings.
Conflict-Free: Ensures no overlaps in teacher schedules or assigned times.
User-Friendly Interface: Input data interactively through the console.
Modular Codebase: Easy to understand, extend, and maintain.
Technologies Used
Python: Core programming language for implementation.
Random Module: For random assignment of classes and schedules.
Object-Oriented Programming (OOP): Used to model teachers, classes, and timetables.
Folder Structure
perl
Copy code
TaskManager/
├── calculation/
│   ├── table.py             # Logic for timetable generation
│   └── _init_.py
├── classes/
│   ├── classs.py            # Class representation
│   ├── teacher.py           # Teacher representation
│   └── _init_.py
├── display/
│   ├── print.py             # Prints the generated timetable
│   └── _init_.py
├── main/
│   ├── main.py              # Main script to run the application
│   └── _init_.py
└── README.md
Example
Input:
Number of teachers: 3
Teacher 1: Gunjal Sir, Subjects: Math, Physics
Teacher 2: Ghodke Sir, Subjects: Chemistry, Biology
Teacher 3: Deshmukh Sir, Subjects: English, History
Output:
A weekly timetable displayed in the console, including:
Lectures and practicals assigned to teachers.
Lunch breaks.
Dedicated slots for teacher and student meetings
