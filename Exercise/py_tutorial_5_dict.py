student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student)
print(student['name'])
print(student['courses'])
print(student.get('name'))  # This will print the value of 'name'
# this will not throw an error if the key does not exist

print(student.get('phone', 'Not Found'))  # This will print 'Not Found' because 'phone' does not exist

student['phone'] = '555-5555'  # This will add a new key-value pair to the dictionary
student['name'] = 'Jane'    # This will change the value of 'name' to 'Jane'

student.update({'name': 'Jane', 'age': 26, 'phone': '555-5555'})    
# This will update the dictionary with the new key-value pairs

del student['age']    # This will delete the key-value pair with the key 'age'

age = student.pop('age')    # This will delete the key-value pair with the key 'age' and store the value in the variable 'age'
# del and return the value
print(age)

print(len(student))    # This will print the number of key-value pairs in the dictionary

print(student.keys())    # This will print the keys of the dictionary
print(student.values())    # This will print the values of the dictionary
print(student.items())    # This will print the key-value pairs of the dictionary

for key in student:
    print(key)
    
for key, value in student.items():
    print(key, value)





