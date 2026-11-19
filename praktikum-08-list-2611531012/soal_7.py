menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []
# Write your code below
for d in range(number_of_days):
    row = []
    for m in range(len(menus)):
        row.append(int(input("Day " + str(d + 1) + ", " + menus[m] + ": ")))
    sales.append(row)

print("Total per day:")
for d in range(number_of_days):
    day_total = 0
    for m in range(len(menus)):
        day_total += sales[d][m]
    print("Day " + str(d + 1) + ":", day_total)

menu_totals = []
for m in range(len(menus)):
    col_total = 0
    for d in range(number_of_days):
        col_total += sales[d][m]
    menu_totals.append((menus[m], col_total))
print("Total per menu:", menu_totals)

best_name = ""
best_total = -1
for name, total in menu_totals:
    if total > best_total:
        best_name = name
        best_total = total
print("Best seller: " + best_name + " (" + str(best_total) + ")")