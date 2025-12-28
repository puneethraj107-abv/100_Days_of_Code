print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    age=int(input("What is your age? "))
    if age<12:
        print("You can ride the rollercoaster and your ticket will be $1")
    elif age>=12:
        print("You can ride the rollercoaster and your ticke will be $5")
    elif age<=18:
        print("You can ride the rollercoaster and your ticket will be $7")
    else:
        print("You can ride the rollercoaster and your ticket will be $18")

else:
    print("Sorry you have to grow taller before you can ride.")
