import random

def generate_timetable(teachers):
    time_slots = ['9am', '10am', '11am', '12pm', '1pm', '2pm', '3pm', '4pm', '5pm']
    week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    timetable = {}
    for time in time_slots:
        timetable[time] = {}
        for day in week_days:
            timetable[time][day] = None

    student_meeting_day = random.choice(week_days)
    timetable['5pm'][student_meeting_day] = 'Student Meeting'

    teacher_meeting_day = random.choice([day for day in week_days if day != student_meeting_day])
    timetable['5pm'][teacher_meeting_day] = 'Teacher Meeting'

    for day in week_days:
        practical_count = 0
        lectures_count = 0
        teacher_lecture_count = {teacher.name: 0 for teacher in teachers}
        
        for time in time_slots:
            if time == '1pm':  
                timetable[time][day] = 'Lunch Break'
                continue
            
            if lectures_count >= 5:
                break

            if timetable[time][day] in ['Student Meeting', 'Teacher Meeting']:  
                continue

            if practical_count < 1:
                available_teachers = [teacher for teacher in teachers if teacher_lecture_count[teacher.name] < 2]
                if available_teachers:
                    chosen_teacher = random.choice(available_teachers)
                    timetable[time][day] = "Practical by " + chosen_teacher.name
                    chosen_teacher.schedule.append((day, time))
                    practical_count += 1
                    teacher_lecture_count[chosen_teacher.name] += 1
            else:  
                available_teachers = [teacher for teacher in teachers if teacher_lecture_count[teacher.name] < 2]
                if available_teachers:
                    chosen_teacher = random.choice(available_teachers)
                    chosen_subject = random.choice(chosen_teacher.subjects)
                    timetable[time][day] = chosen_subject + " by " + chosen_teacher.name
                    chosen_teacher.schedule.append((day, time))
                    lectures_count += 1
                    teacher_lecture_count[chosen_teacher.name] += 1
               
    return timetable
