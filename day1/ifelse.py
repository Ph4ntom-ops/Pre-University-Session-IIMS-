import sys

age = input("Enter your age: ")
try:
    age = int(age)
    if age < 0:
        print("Negative")
    elif age > 0:
        print("Positive")
    else:
        print("Zero")
except ValueError:
    sys.exit("Enter a number!")









