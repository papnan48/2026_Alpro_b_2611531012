# Name: Afnan feyza
# NIM: 2611531012
# Question 6
full_name = "Afnan Feyza"
nim = "2611531012"
clean = full_name.strip()
space = clean.find(" ")
if space == -1:
    first_name = clean
else:
    first_name = clean[:space]
username = first_name.lower() + nim[-3:]
print(username)
# Build the username: first name in lowercase + last 3 digits of the NIM.
# Do not use split().
