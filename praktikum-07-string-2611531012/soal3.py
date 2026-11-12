# Name: Afnan feyza
# NIM: 2611531012
# Question 3 (A)
text = "Informatika"
print(text[10])
print(text.upper())
print(text[0:20])

# Question 3 (B)
text = "Afnan Feyza"
count = 0
for char in text:
    if char in "aiueoAIUEO":
        count = count + 1
print("Vowels:", count)
