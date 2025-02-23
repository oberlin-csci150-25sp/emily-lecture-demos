import random

won = False # variable for game ongoing / game over
goal = random.randint(0, 9)

while not won: # run indefinitely until game over
  guess = int(input("Guess a number between 1-9: "))
  if guess == goal:
    print("You win!")
    # clicker question: what goes here? 