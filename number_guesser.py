import random

number = random.randint(1,100)
attempts = 0
print("I picked a number 1 and 100,Guess it!")

while True:
    guess = int(input("Your guess: "))
    attempts = attempts + 1

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"correct! You got it in {attempts} attempts.")
        break