def print_timetable(timetable):
    print("Time  | ", end="")
    print("      | ".join(timetable['9am'].keys()))
    print("-------------------------------------------------")
    for time, schedule in timetable.items():
        row = time + " | "
        row += " | ".join(task if task else "No class" for task in schedule.values())
        print(row)
