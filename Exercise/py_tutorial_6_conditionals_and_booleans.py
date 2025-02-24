if True:
    print('Conditional was True')
    
if False:
    print('Conditional was False')  # This will not print anything
    
language = 'Python'

if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
else:
    print('No match')
    
user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')
    
user = 'Admin'
logged_in = False

if not logged_in:
    print('Please log in')
else:
    print('Bad Creds')
    
a = [1, 2, 3]
b = [1, 2, 3]

print(id(a))   # This will print the memory address of the list
print(id(b))   # This will print the memory address of the list
print(a is b)  # This will print False because the memory addresses are different
print(a == b) # This will print True because the values are the same

b = a
print(id(a))
print(id(b))
print(a is b)


# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), []
    # Any empty mapping. For example, {}

condition = None

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

