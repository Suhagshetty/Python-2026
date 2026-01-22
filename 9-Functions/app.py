name = "Suhag shetty"
def greetUser():
    print("Hello ",name)
    print("How are you?")
greetUser()
greetUser()

# Function to check if number is even or not

def guessEven(num):
    if num%2==0:
        print("Even")
    else:
        print("Odd")
guessEven(2)
guessEven(3)

# Function to return bioData
def bioData(name,age,job):
    print("Hello ",name,"age is ",age,"I am a",job)
bioData("Suhag",22,"SWE")

# Return statement:- Sqaure

def square(num):
    return num*num
print(square(2))
print(square(3))
