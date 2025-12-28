print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill=0

if height >= 120:
    print("you can ride the rollercoaster")
    age=int(input("What is your age? "))
    if age <=12:
        bill+=5
        print(f"you\'re ticket will be ${bill}")
    elif age<=18:
        bill+=7
        print(f"you\'re ticket will be ${bill}")
    elif age>=45 and age<=55:
        print("everything is gonna be okay,the ride is on us")
    else:
        bill+=12
        print(f"you\'re ticket will be ${bill}")
else:
    print("comeback when you are grown up kid")