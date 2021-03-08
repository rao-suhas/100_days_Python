from art import logo
print(logo)
print("----------------------------------------------")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = "foo"

# Caesar cipher function
def caesar_cipher(direction, text, shift):
  mod_text = ""
  # Condition for encoding and decoding
  for letter in text:
    # Condition to preserve spaces/chars/numbers
    if letter in alphabet:
      position = alphabet.index(letter)
      if direction == "encode":
        new_position = position + shift
      elif direction == "decode":
        new_position = position - shift
      mod_text += alphabet[new_position]
    else:
      mod_text += letter
  print(f"The {direction}d text is: {mod_text}")

# Set a while loop till the user types in stop
while(direction != "exit"):
  # Get the inputs
  direction = input("OPTIONS: \n'encode' to encrypt, \n'decode' to decrypt \n'exit' to end the program:\n").lower()
  print("-----------------------------------------")
  
  # Check for exit command
  if direction == "exit":
    break
  
  text = input("Type your message:\n").lower()
  print("-----------------------------------------")
  shift = int(input("Type the shift number: "))

  # Handle large shift number entered by user
  if shift > 26:
    shift = shift % 26

  print("-----------------------------------------")  
  caesar_cipher(direction=direction, text=text, shift=shift)
  print("=========================================")
