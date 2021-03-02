# Get the names of the people
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

# Count the number of TRUE LOVE chars separately and join them together to get the percentage
joint_name = name1 + " " + name2
print(joint_name)

digit1 = joint_name.count("t")+joint_name.count("r")+joint_name.count("u")+joint_name.count("e")

digit2 = joint_name.count("l")+joint_name.count("o")+joint_name.count("v")+joint_name.count("e")

print(f"Your compatibility score is {str(digit1)+str(digit2)}")