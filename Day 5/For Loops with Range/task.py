score = 0
for number in range(1,101):
    score = number
    if score % 3 == 0:
        score= "fizz"
    if score % 5 == 0:
        score ="buzz"
        print(f"{score}")