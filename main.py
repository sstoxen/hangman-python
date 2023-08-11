from random import choice


def print_board(guessed: str, secret_word: str) -> int:
  """Prints the current board to the screen based on the letters guessed."""
  blanks: int = 0
  print("Word ", end="")
  for char in secret_word:
    if char in guessed:
      print(char, end="")
    else:
      print("_", end="")
      blanks += 1
  print()  # Adds a blank line
  return blanks


def get_input() -> str:
  """
  Gets the input from the user. If a non-alphanumeric character is used, this will loop until one is used.
  This will possibly cause the program to run out of memory since it is recursive but the amount of memory used each
  time is very low so that would take a very large amount of entries.
  """
  guess: str = input("Enter a letter: ")
  return guess if guess.isalpha() else get_input()


def get_remaining_tries(guess: str, word: str, old_try_count: int) -> int:
  """Calculates what the remaining number of guesses should be based off the current state of the game is."""
  return old_try_count - (1 if guess not in word else 0)


def run_game():
  secret_word: str = choice(['apple', 'secret', 'banana']).lower()
  username: str = input("What is your name? ")
  print(f"Welcome to hangman, {username}")

  # Setup
  guessed: str = ""
  remaining_tries: int = 3
  finished = False
  print_board(guessed, secret_word)
  while not finished:
    guess = get_input()
    print(f"guess is {guess}")

    # I know...It's not good to have a bunch of nested if-else conditions but tough!
    if len(guess) > 1:
      if guess == secret_word:
        print("Spot on!")
        return
      else:
        print("Nice try...WRONG!")
        remaining_tries -= 1
    else:
      guessed += guess
      if print_board(guessed, secret_word) == 0:
        print("You got it!")
        return
      else:
        remaining_tries = get_remaining_tries(guess, secret_word, remaining_tries)
    print(remaining_tries)
    if remaining_tries == 0:
      print("Well...You didn't get it. Better luck next time.")
      return


if __name__ == "__main__":
  run_game()
