# List Methods

number = [1,2,3,4,5]
number.append(7)
print(number)

# Insert:- [0,10] here 0 is the index we need to specify where we need to add the value
number.insert(0,10)
print(number)

# Remove
number.remove(1)
print(number)

# Clear:- removes all the value
# print(number.clear())

# POP:- removes values at the end
number.pop()
print(number)

# Index:- returns the index where we specify the value 
print(number.index(3))

# In:- check if value is present or not:- returns a BOOLEAN value.
print(20 in number)

# SORT:- sorts the number
num = [1,9,8,7,6,5]
num.sort()
print(num)

# Reverse:- reverses numbers
revereseNumber = [9,8,7,6,5]
revereseNumber.reverse()
print(revereseNumber)