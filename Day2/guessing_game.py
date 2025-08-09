name = input("Enter name: ")
secrete_number = 8
while True:
    guess = int(input("guess a number from 1-10: "))

    if guess == secrete_number:
        print(f"{name.capitalize()} guessed correctly")

    else:
        print("wrong number. try again")