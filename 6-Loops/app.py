# The While Loop

secretNumber = 9
guessCount = 0
guessLimit = 3
while guessCount < guessLimit:
    guess = int(input("Guess: "))
    guessCount += 1
    if guess == secretNumber:
        print("You Won!")
        break
else:
    print("You Lost!")

# For Loops

for name in ["Suhag","Shetty","Jake"]:
    print(name)

# looping through Numbers

for numbers in [1,2,3,4,5]:
    print(numbers)

# Even Numbers printing
for even in [1,2,3,4]:
    if even % 2 == 0:
        print("Even numbers here are, ",even)

# To PRINT numbers from 0 to 10
for tens in range(10):
    print(tens)

# STEPS FORWARD (x,y,"specify the gap ")
for steps in range(6,10,2):
    print(steps)

# Looping through evens in 100
for evens in range(100):
   if evens%2==0:
    print("The even numbesr from 1 to 100: ",evens)


# NESTED LOOPS