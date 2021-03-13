from art import logo

print(logo)
# Addition
def add(n1, n2):
  return n1 + n2

# Subtraction
def subtract(n1, n2):
  return n1 - n2

# Multiplication
def multiply(n1, n2):
  return n1*n2

# Division
def divide(n1, n2):
  if n2 != 0:
    return n1/n2
  else:
    return "Math Error"

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

continue_option = "n"
while True:
  # Get the inputs
  if continue_option == "n":
    num1 = int(input("What's the first number?: "))

  num2 = int(input("What's the second number?: "))

  for key in operations:
    print(key)

  # Get the operation to perform
  operation_symbol = input("Pick an operation from the above list: ")

  # Assign the function based on the operation using the dictionary
  function = operations[operation_symbol]
  result = function(num1, num2)
  print(f"{num1} {operation_symbol} {num2} = {result}")

  continue_option = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start fresh or 'exit' to close the program:\n").lower()

  if continue_option == "y":
    num1 = result
  elif continue_option == "n":
    result = 0
  elif continue_option == "exit":
    break
