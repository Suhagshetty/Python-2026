# Type conversion in Python 

birthYear = input("Enter your Birth year:- ")
print(type(birthYear))
age = 2026 - int(birthYear)
print(type(birthYear))
print("You were born in ",birthYear," so your age is ",age)

# WEIGHT CONVERSION

weightInLbs = input("Enter your weight in LBS:- ")
weightInKg  = int(weightInLbs)*0.45
print("Your weight in kgs is ",weightInKg)