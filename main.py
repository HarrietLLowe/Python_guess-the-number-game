import random
from art import logo

NUMBER = random.randint(1,100)
GAME_OVER = False

def play_easy():
  global NUMBER
  global GAME_OVER
  guesses_left = 10
  print("You have 10 guesses left.")
  while not GAME_OVER:
    guess = int(input("Make a guess: "))
    if guess == NUMBER:
      print(f"Well done! You guessed {NUMBER} correctly.")
      GAME_OVER = True
    elif guess > NUMBER:
      print("Too high.")
      guesses_left -= 1
      print(f"You have {guesses_left} guesses left!")
      if guesses_left == 0:
        print("You've run out of guesses, you lose!")
        GAME_OVER = True
    elif guess < NUMBER:
      print("Too low.")
      guesses_left -= 1
      print(f"You have {guesses_left} guesses left!")
      if guesses_left == 0:
        print("You've run out of guesses, you lose!")
        GAME_OVER = True
    else:
      print("Invalid entry.")

def play_hard():
  global NUMBER
  global GAME_OVER
  guesses_left = 5
  print("You have 5 guesses left.")
  while not GAME_OVER:
    guess = int(input("Make a guess: "))
    if guess == NUMBER:
      print(f"Well done! You guessed {NUMBER} correctly.")
      GAME_OVER = True
    elif guess > NUMBER:
      print("Too high.")
      guesses_left -= 1
      print(f"You have {guesses_left} guesses left!")
      if guesses_left == 0:
        print("You've run out of guesses, you lose!")
        GAME_OVER = True
    elif guess < NUMBER:
      print("Too low.")
      guesses_left -= 1
      print(f"You have {guesses_left} guesses left!")
      if guesses_left == 0:
        print("You've run out of guesses, you lose!")
        GAME_OVER = True
    else:
      print("Invalid entry.")

def main():
  print(logo)
  print("Welcome to the Number Guessing Game!\n\nI am thinking of a number between 1 and 100.")
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if difficulty == "easy":
    play_easy()
  elif difficulty == "hard":
    play_hard()
  else:
    print("Not recognised. Try again.")

main()