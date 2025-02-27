def hello_func():
    pass

hello_func()

print(hello_func)   # <function hello_func at 0x0000021D3D3A3D08>

print(hello_func()) # None

def hello_func():
    print('Hello Function!')
    
hello_func()    # Hello Function!
# no need to use print() to call the function

def hello_func():
    return 'Hello Function!' # the function equal to the string

print(hello_func()) # Hello Function!

def hello_func(greeting):
    return '{} Function.'.format(greeting)
print(hello_func('Hi')) # Hi Function.

def hello_func(greeting, name = 'You'): # default value
    return '{} {}'.format(greeting, name)  
print(hello_func('Hi')) # Hi You
print(hello_func('Hi', name = 'Corey')) # Hi Corey

def student_info(*args, **kwargs): # *args for tuple, **kwargs for dictionary
    print(args)
    print(kwargs)   

student_info('Math', 'Art', name = 'John', age = 22) 
# ('Math', 'Art') {'name': 'John', 'age': 22}

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info(courses, info)
# (['Math', 'Art'], {'name': 'John', 'age': 22}) {}


student_info(*courses, **info)  # unpacking
# ('Math', 'Art') {'name': 'John', 'age': 22}


month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if not 1 <= month <= 12:
        return 'Invalid Month'
    
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]

print(days_in_month(2017, 2)) # 28
print(days_in_month(2020, 2)) # 29
print(days_in_month(2000, 2)) # 29

 
