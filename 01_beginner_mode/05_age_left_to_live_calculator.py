# Get the age of the person
age = input("What is your current age?")

#Calculate days, weeks & months left if average lifespan is 90 years

age = int(age)
years_remaining = 90-age

days = years_remaining*365
weeks = years_remaining*52
months = years_remaining*12

print(f"You have {days},\n {weeks} weeks,\n {months} months left")
