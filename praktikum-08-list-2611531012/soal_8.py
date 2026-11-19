number_of_rows = 4
seats_per_row = 5
# Write your code below
seats = []
for r in range(number_of_rows):
    seats.append(["."] * seats_per_row)   # setiap baris = list baru

def show():
    for r in range(number_of_rows):
        print("Row " + str(r + 1) + ":", " ".join(seats[r]))

while True:
    show()
    row = int(input("Row (0 to stop): "))
    if row == 0:
        break
    seat = int(input("Seat: "))
    if row < 1 or row > number_of_rows or seat < 1 or seat > seats_per_row:
        print("Invalid seat.")
    elif seats[row - 1][seat - 1] == "X":
        print("Seat already taken.")
    else:
        seats[row - 1][seat - 1] = "X"
        print("Seat booked.")

taken = 0
for r in range(number_of_rows):
    for s in range(seats_per_row):
        if seats[r][s] == "X":
            taken += 1
print("Seats taken:", taken)