LAST_DIGIT = 2 # change to the last digit of your NIM
daily_limit = 30000 + LAST_DIGIT * 1000
expenses = []
# Write your code below
for day in range(1, 8):
    expenses.append(int(input("Day " + str(day) + ": ")))

total = 0
for e in expenses:
    total = total + e
average = total / len(expenses)

highest_day = 1
highest_value = expenses[0]
above_limit = 0
for i in range(len(expenses)):
    if expenses[i] > highest_value:
        highest_value = expenses[i]
        highest_day = i + 1
    if expenses[i] > daily_limit:
        above_limit += 1

print("Daily limit:", daily_limit)
print("Total:", total)
print("Average:", round(average, 1))
print("Highest: day", highest_day, "(" + str(highest_value) + ")")
print("Days above limit:", above_limit)