#Number Guessing Game
A simple, interactive command-line Python game where the player tries to guess a randomly generated number within a user-defined range. The player has a limited number of attempts to find the correct number.

#Features
Dynamic Range: The user defines the minimum (Lower Bound) and maximum (Upper Bound) numbers.

Limited Attempts: The player gets exactly 7 chances to guess the number.

Smart Feedback: After each incorrect guess, the game hints whether the actual number is higher or lower, and displays the remaining number of attempts.

#How to Run
Prerequisites: Make sure you have Python 3 installed on your system.

Save the Script: Save the code into a file named guessing_game.py.

Execute the Game: Open your terminal or command prompt, navigate to the folder where the file is saved, and run:

Bash
python guessing_game.py

#Gameplay Rules
Upon starting, enter the desired Lower Bound and Upper Bound.

The system will randomly pick a number within that range (inclusive).

You will have 7 attempts to guess the exact number.

Feedback guide:

Too high!: Your guess is greater than the target number.

Too low!: Your guess is smaller than the target number.

Correct!: You win! The game will show how many attempts it took you.

If you run out of 7 chances without guessing correctly, the game will reveal the number and end.

#Example Output

Hi! Welcome to the Number Guessing Game.
You have 7 chances to guess the number. Let's start!

Enter the Lower Bound: 1
Enter the Upper Bound: 50

You have 7 chances to guess the number between 1 and 50. Let's start!
Enter your guess: 25
Too high! Try a lower number.
You have 6 guesses left.

Enter your guess: 12
Correct! The number is 12. You guessed it in 2 attempts.