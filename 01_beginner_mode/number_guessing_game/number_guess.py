import random

logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""

print(logo)

# define a function that compares the numbers
def compare_num(chosen, guessed):
  global game_ended
  global num_lives
  if chosen == guessed:
    game_ended = True
    print(f"You win! That was a correct guess \nThe number was: {chosen}")
  elif chosen != guessed and chosen < guessed:
    num_lives = num_lives - 1
    if num_lives == 0:
      print(f"You lost, Game over \nThe number was: {chosen}")
      game_ended = True
    else:
      print("Too High, try again.")
      print(f"You have {num_lives} lives remaining")
  elif chosen != guessed and chosen > guessed:
    num_lives = num_lives - 1
    if num_lives == 0:
      print(f"You lost, Game over \nThe number was: {chosen}")
      game_ended = True
    else:
      print("Too Low, try again.")
      print(f"You have {num_lives} lives remaining")


print("Welcome to the number guessing game")
difficulty = input("Choose the game level: 'easy' or 'hard': ").lower()

# Set the lives based on difficulty
if difficulty == 'easy':
  num_lives = 8
elif difficulty == 'hard':
  num_lives = 5

num_chosen = random.randint(1, 100)
game_ended = False

while(game_ended == False):
  num_guess = int(input("Guess a number between 1 and 100: "))
  compare_num(num_chosen, num_guess)
