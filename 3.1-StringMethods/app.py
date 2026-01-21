# Length:- Len is a general purpose operator
name = "John Smith"
print(len(name))

# Upper and lowerCase:- these dont modify the og string they just replaces them.
print(name)
print(name.upper())
print(name.lower())
print(name)

# Find:- returns the index of the specified :- Its case sensitive. if ot could not find the specified thing shows -1

course = "Complete Python 'Course'"
print(course.find("r"))

# Replace
print(course)
print(course.replace("Complete Python 'Course'","Python For People"))

# In:- its similar to find methods but instead of index it returns boolean value
print("python" in course) 
print("Python" in  course)