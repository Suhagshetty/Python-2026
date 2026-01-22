# Lists:- Lists in Python are mutable, ordered collections that store multiple items in a single variable using square brackets. It returns a new list does not change the og list

names = ["Suhag","Karan","Prashanth","Mukesh","Uday"]
print(names[0])
print(names[3])
print(names[-1])

# Retrieving names between (-1 at the last)
print(names[1:3])
print(names)

# Program to find largest number in a list
largestNumber = [1, 2, 3, 4, 5]
max_val = largestNumber[0]
for num in largestNumber:
    if num > max_val:
        max_val = num
print(max_val)  

# Check for duplicates
my_list = [1, 2, 3, 5, 6, 7, 5, 2]
seen = []
duplicates = []

for item in my_list:
    if item in seen:
        duplicates.append(item)
    else:
        seen.append(item)

print("Duplicates:", duplicates)  # Output: [5, 2]

