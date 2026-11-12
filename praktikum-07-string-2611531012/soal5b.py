# Name: Afnan feyza
# NIM: 2611531012
# Question 5 (B)
nim = input("NIM: ")
if len(nim) == 10 and nim.isdigit():
    print("Valid, intake year 20" + nim[:2])
else:
    print("Invalid NIM")