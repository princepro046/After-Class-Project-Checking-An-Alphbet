#Checking wheter its an alphabet or not
def is_alphabet(char):
    # Check if the character is between 'a' to 'z' or 'A' to 'Z' using comparison operators
    return ('a' <= char <= 'z') or ('A' <= char <= 'Z')

# Taking input from the user
char = input("Enter a character: ")

# Check if the character is a single character
if len(char) == 1:
    if is_alphabet(char):
        print(f"The character '{char}' is an alphabet.")
    else:
        print(f"The character '{char}' is not an alphabet.")
else:
    print("Please enter exactly one character.")
