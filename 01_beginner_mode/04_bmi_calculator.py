# Get the height and weight input
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

# Calculate the BMI
BMI = int(float(weight)/(float(height)**2))

print(BMI)