import random

print("Hi! Welcome to the Number Guessing Game.\nYou have 7 chances to guess the number. Let's start!")

low = int(input("Enter the Lower Bound: "))
high = int(input("Enter the Upper Bound: "))

print(f"\nYou have 7 chances to guess the number between {low} and {high}. Let's start!")

num = random.randint(low, high)

gc = 7

ch = 0

while ch < gc:
    guess = int(input("Enter your guess: "))
    ch += 1

    if guess == num:
        print(f'Correct! The number is {num}. You guessed it in {ch} attempts.')
        break
    elif guess > num:
        print('Too high! Try a lower number.')
    else:
        print('Too low! Try a higher number.')

    remaining = gc - ch
    if remaining > 0:
        print(f'You have {remaining} guesses left.')
else:
    print(f'Sorry! The number was {num}. Better luck next time.')