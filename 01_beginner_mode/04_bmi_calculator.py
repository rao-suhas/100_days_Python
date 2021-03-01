# Get the height and weight of user
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

# Calculate the bmi
bmi = weight/(height**2)

# Refer the chart and show the corresponding output
if bmi < 18.5:
  print("Underweight")
elif bmi >= 18.5 and bmi < 25:
  print("normal weight")
elif bmi >= 25 and bmi < 30:
  print("Slightly Overweight")
elif bmi >= 30 and bmi < 35:
  print("Obese")
elif bmi >=35:
  print("Clinically Obese")
