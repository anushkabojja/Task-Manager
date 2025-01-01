# Task Manager

## Description

The Task Manager is a Python-based project designed to automatically generate and manage college timetables. It accounts for teachers, subjects, and specific scheduling rules to create an efficient, conflict-free schedule for the entire week. The tool aims to simplify the process of timetable creation while ensuring fair distribution of work among teachers.

## Features

- *Dynamic Timetable Generation*: Automatically generates a timetable based on the number of teachers, their subjects, and the classes.
- *Customizable Scheduling*:
  - Includes practical sessions, lectures, and meetings.
  - Guarantees one practical session per day and proper lunch breaks.
  - Allocates special slots for teacher and student meetings.
- *Conflict-Free*: Ensures no overlaps in teacher schedules or assigned times.
- *User-Friendly Interface*: Input data interactively through the console.
- *Modular Codebase*: Easy to understand, extend, and maintain.

## Technologies Used

- *Python*: Core programming language for implementation.
- *Random Module*: For random assignment of classes and schedules.
- *Object-Oriented Programming (OOP)*: Used to model teachers, classes, and timetables.

## Folder Structure

TaskManager/ ├── calculation/ │ ├── table.py # Logic for timetable generation │ └── init.py # Initialization for the calculation module ├── classes/ │ ├── classs.py # Class representation │ ├── teacher.py # Teacher representation │ └── init.py # Initialization for the classes module ├── display/ │ ├── print.py # Prints the generated timetable │ └── init.py # Initialization for the display module ├── main/ │ ├── main.py # Main script to run the application │ └── init.py # Initialization for the main module └── README.md 
## Future Updates

- *Teacher Availability*: Integration of teacher availability for more accurate scheduling.
- *Automated Reminders*: Email or text-based reminders for scheduled classes and meetings.
- *GUI Interface*: Implementation of a graphical user interface (GUI) for easier user interaction.
- *Advanced Conflict Resolution*: Enhanced algorithms for resolving complex scheduling conflicts.
- *Web Application*: Development of a web-based version of the Task Manager for broader accessibility.
