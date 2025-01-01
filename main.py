from calculation.table import generate_timetable
from classes.teacher import Teacher
from classes.classs import Class
from display.print import print_timetable

def main():
    num_teachers = int(input("Enter the number of teachers: "))
    teachers = []

    for _ in range(num_teachers):
        name = input("Enter teacher's name: ")
        subjects = input("Enter subjects taught by the teacher (comma-separated): ").split(",")
        teachers.append(Teacher(name, subjects))
    
    timetable = generate_timetable(teachers)
    print_timetable(timetable)
main()
