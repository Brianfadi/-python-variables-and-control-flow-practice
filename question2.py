from PIL.ImImagePlugin import number


# Ask the user for a number
number = int(input("Enter a number: "))

# Check if the number is odd or even
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
