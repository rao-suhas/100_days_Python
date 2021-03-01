# Get the year input
year = int(input("Which year do you want to check? "))

# Check if the year is leap year
if year%4 == 0 and year%100 !=0:
  print(f"{year} is a leap year")
elif year%4 == 0 and year%100 == 0 and year%400 == 0:
  print(f"{year} is a leap year")
elif year%4 == 0 and year%100 == 0 and year%400 != 0:
  print(f"{year} is not a leap year")
elif year%4 !=0:
  print(f"{year} is not a leap year")

### Conditions for Leap year
# 1. If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
# 2. If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
# 3. If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
# 4. The year is a leap year (it has 366 days).
# 5. The year is not a leap year (it has 365 days).
###
