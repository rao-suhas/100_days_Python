print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

Q1 = input("which way do you want to choose? left or right?\n").lower()

if Q1 == "left":
  Q2 = input("You're standing at the entrance of a broken bridge.\nThe water beneath is not that deep.\nWhat do you want to do? Swim or Wait?\n").lower()
  if Q2 == "swim":
    Q3 = input("You reach the other side of the shore and you find 3 enchanted doors!\nWhich door do you want to choose? Red or Blue or Yellow?\n").lower()
    if Q3 == "red":
      print("You are teleported into an Ice World with no way back!\nDeath by Hypothermia.\nGAME OVER!\n")
    elif Q3 == "blue":
      print("You are teleported into Lava World with no way back!\nDeath by falling into Lava.\nGAME OVER!\n")
    elif Q3 == "yellow":
      print("A huge wooden box filled with ancient tressure appears in front of you!\nCongratulations! You win the game!")
    else:
      print("Ehh.. Wrong answer! you're dead.. just cuz.. GAME OVER!!")
  else:
    print("You fell asleep while waiting and a pride of lions attacked & killed you. GAME OVER!\n")
else:
  print("You travelled 5m and fell into a hole! GAME OVER!\n")
