############### Blackjack Project #####################
import random 
from art import logo

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################
print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
  # cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  """Takes a list of cards and returns the score calculated from the cards"""
  # Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  # Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  if user_score == computer_score:
    return "draw!"
  elif computer_score == 0:
    return "You Lost! the opponent has a blackjack"
  elif user_score == 0:
    return "You Win! You have a blackjack!"
  elif user_score > 21:
    return "You Lose! went over 21"
  elif computer_score > 21:
    return "You Won! Computer went over 21"
  elif user_score > computer_score:
    return "You win!"
  else:
    return "You Lose!"

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
user_cards = []
computer_cards = []
is_gameover = False

for _ in range(2):
  user_cards.append(deal_card())
  computer_cards.append(deal_card())

while not is_gameover:
  user_score = calculate_score(user_cards)
  computer_score = calculate_score(computer_cards)
  print(f" Your cards: {user_cards}, Current score: {user_score}")
  print(f" Computer's first card: {computer_cards[0]}")

  if user_score == 0 or computer_score == 0 or user_score >21:
    is_gameover = True
  else:
    user_should_deal = input("Type 'y' to get another card or 'n' to pass: ").lower()
    if user_should_deal == "y":
      user_cards.append(deal_card())
    else:
      is_gameover = True

while computer_score != 0 and computer_score < 17:
  computer_cards.append(deal_card())
  # print(f" Computer's first 2 card: {computer_cards[:2]}")
  computer_score = calculate_score(computer_cards)
#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

print(f" Your final hand: {user_cards}, Final score: {user_score}")
print(f" Computer's final hand: {computer_cards}, Final score: {computer_score}")
print(compare(user_score, computer_score))
