name = input("Enter your name: ").strip().title()
age = int(input("Enter your age: ").strip())

def greetings(name, age):
    next_year_age = str(age + 1)
    print("Hello " + name + ", you'll be turning " + next_year_age + " next year.")

greetings(name,age)
