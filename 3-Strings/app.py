from email import message


course = 'This is the complete python course by "Mosh"'
print(course)
# This is one was handling strings use '' when u want to specify certain things in quotes.
courseDesc = "This is the best course to learn 'python'"
print(courseDesc)
# vice versa

# MULTI LINE STRING '''
email = '''
Hi Smith,
This is Jacob from the Bay Area how is it going?
Have you merged the PR i had raised
'''
print(email)

# Indexing and negative indexing

name = "Suhag Shetty"
print(name[0]) 
# Negative index:- gives us to value from the reverse order
print(name[-1])
# name = "Suhag Shetty"
# print(name[0])    # 'S'
# print(name[-0])   # 'S' (same as [0])
# print(name[-1])   # 'y'


# Formatted Strings

firstName = "Suhag"
lastName = "Shetty"
message = f'{firstName} {lastName} is a coder'
print(message)

# f is the prefix and use {to add value to display}