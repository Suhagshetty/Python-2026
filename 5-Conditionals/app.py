itsHot = False
isCold = False
if itsHot:
    print("Its a Hot Day")
    print("Drink Water")
elif isCold:
    print("Its a Cold Day")
    print("Wear a Hoodie")
else:
    print("Its a Lovely Day")
print("Enjoy your Day")

# Assignment
priceOfHouse  = 1000000
hasGoodCredit = True
if hasGoodCredit:
    print ("The buyer pays 10% as down payment which is $",priceOfHouse*0.10,"dollar")
else:
    print("The buyer has to pay 20% as down payment which is $",priceOfHouse*0.20,"dollar")

# Logical Operators [ AND OR NOT]

hasGoodCredit   = True
hasCriminalRecord  = True
if hasGoodCredit and hasCriminalRecord:
    print("Good for loan")

hasGoodCredit = True
hasCriminalRecord = False
if hasCriminalRecord or hasGoodCredit:
    print("Its okay there is a chance")

not hasCriminalRecord
print(hasCriminalRecord)

# Comparison Operator in Python

temperature = 15
if(temperature>=30):
    print("ITS A HOT DAY")
elif(temperature<10):
    print("ITS A COLD DAY")
else:
    print("ITS NEITHER HOT OR COLD")

# Assignment 

nameCheck = "X"
if (len(nameCheck) <=3 ):
    print("TOO LESS CHARACTERS")
elif (len(nameCheck)>50):
    print("MAX CHARACTERS")
else:
    print("NAME LOOKS GOOD")

# WEIGHT CONVERTER PROGRAM

weight  = int(input("Enter your weight"))
unit = input('(L)bs or (K)gs: ')
if unit.upper() == "L":
    convertedWeight = weight*0.45
    print(f"You are {convertedWeight} kilos")
else:
    convertedWeight = weight/0.45
    print(f"You are {convertedWeight} pounds")