# Name: Afnan feyza
# NIM: 2611531012
# Question Bonus
sentence = input("Sentence: ")
clean = sentence.replace(" ", "").lower()
if clean == clean[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")