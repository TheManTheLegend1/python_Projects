# No Vowels
# Demonstrates creating new strings with a for loop

message = raw_input("Enter a message: ")
new_message = ""
VOWELS = "aeiou"

print()
for letter in message:
    if letter.lower() not in VOWELS:
        new_message += letter
        print"A new string has been created:", new_message

print"\nYour message without vowels is:", new_message

raw_input("\n\nPress enter to exit")
