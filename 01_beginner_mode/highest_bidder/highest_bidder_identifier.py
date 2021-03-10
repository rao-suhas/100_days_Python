from art import logo
import os

print(logo)

bidders = []

# Function that creates dictionaries in the bidders list
def add_bidders(name, bid):
  temp_dict = {"name": name, "bid_value": bid}
  bidders.append(temp_dict)

while True:
  # Get the inputs
  name = input("What is your name?: ").lower()
  bid_val = int(input("What is your bid?: $"))

  # Call the add bidder function
  add_bidders(name, bid_val)

  # Check for other bidders
  other_bidders = input("Are there other bidders? 'yes' or 'no': ").lower()

  if other_bidders == "no":
    break
  elif other_bidders == "yes":
    clear = lambda: os.system('cls')
    clear()

max_bid = 0
winner = ""

for bidder in bidders:
  if bidder["bid_value"] > max_bid:
    max_bid = bidder["bid_value"]
    winner = bidder["name"]

print(f"Winner is {winner}")
print(bidders)
