# Name: Afnan feyza
# NIM: 2611531012
# Question 7
#Display a student card with your own data, in exactly the format of the example below.
#The card is 30 characters wide, with the title centered.
#Labels are left-aligned in a width of 10 characters.
#Store the name in lowercase in the variable name, then display it with title().
#Use the username from Question 6. Take the intake year from the NIM with slicing.
name = "Afnan Feyza"
nim = "2611531012"
space = name.find(" ")
if space == -1:
    first_name = name
else:
    first_name = name[:space]
username = first_name.lower() + nim[-3:]
intake_year = "20" + nim[:2]
print("=" * 30)
print("STUDENT CARD".center(30))
print("=" * 30)
print(f"{'Name:':<10}{name.title()}")
print(f"{'NIM:':<10}{nim}")
print(f"{'Username:':<10}{username}")
print(f"{'Intake Year:':<10}{intake_year}")
print("=" * 30)