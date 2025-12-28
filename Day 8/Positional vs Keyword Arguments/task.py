# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")

# function with more than one input
def greet_with(name, age, location):
    print(f"Hello {name}, you are {age} years old.")
    print(f"you live in {location}")

greet_with("Jack Bauer",11,"bengaluru")
greet_with(age="Jack Bauer",name=11,location="bengaluru")
