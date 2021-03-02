# Welcome message
print("Welcome to the tip calculator")

# Get the bill, tip percentage & number of split
bill = float(input("What is the total bill? "))
tip_percent = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
split_num = int(input("How many people to split the bill? "))

#Calculate the amount to be paid by each person
amount = round((bill + (bill*tip_percent)/100)/split_num, 2)

print("Each person should pay: {:.2f}".format(amount))