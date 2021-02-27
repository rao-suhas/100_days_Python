# Get the 2 digit input number
two_digit_number = input("Type a two digit number: ")

#Convert the given number to a string
string_two_digit_number = str(two_digit_number)

#Subscript the string and add those two together
print(int(string_two_digit_number[0]) + 
int(string_two_digit_number[1]))