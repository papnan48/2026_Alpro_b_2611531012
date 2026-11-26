schedule = {
    "Monday": ["Algorithms", "Calculus"],
    "Tuesday": ["English"],
    "Wednesday": ["Algorithms", "Physics", "Discrete Math"],
    "Thursday": ["Physics", "Calculus"],
    "Friday": ["Discrete Math"]
}

busiest_day = max(schedule, key=lambda day: len(schedule[day]))
jumlah = len(schedule[busiest_day])
print(f"Busiest day: {busiest_day} ({jumlah} courses)")

course = input("Ketikkan nama matkul: ")

jumlah_hari = 0
for day in schedule:
    if course in schedule[day]:
        jumlah_hari += 1

print(f"{course}: {jumlah_hari} days")