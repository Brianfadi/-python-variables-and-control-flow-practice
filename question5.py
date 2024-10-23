# Ask the user to enter the age
age = int(input("Enter your age: "))

# Check if the person is a minor, adult, or senior
if age < 18:
    print("You are a minor.")
elif 18 <= age <= 65:
    print("You are an adult.")
else:
    print("You are a senior.")
