def print_timetable(timetable, class_name):
    print(f"Timetable for {class_name}:\n")
    print("Time      | " + " | ".join(timetable['9am'].keys()))
    print("-------------------------------------------------")
    for time, schedule in timetable.items():
        row = f"{time:8} | " + " | ".join(task if task else "No class" for task in schedule.values())
        print(row)