courses = ['History', 'Math', 'Physics', 'CompSci'] 
print(courses)
print(len(courses))
print(courses[0])
print(courses[3])
print(courses[-1])
# print(courses[4])    # This will throw an error because the index is out of range
print(courses[0:2])   # This will print the first two elements of the list
print(courses[2:])  # This will print the list from the 3rd element to the end

courses.append('Art')    # This will add 'Art' to the end of the list
courses.insert(0, 'Art')    # This will add 'Art' to the beginning of the list
print(courses)

courses_2 = ['Education', 'Chemistry']
courses.insert(0, courses_2)    # This will add the list 'courses_2' to the beginning of the list
courses.extend(courses_2)    # This will add the elements of 'courses_2' to the end of the list
print(courses)

courses.remove('Math')    # This will remove 'Math' from the list
print(courses)

courses.pop()    # This will remove the last element from the list
print(courses)

courses.reverse()    # This will reverse the list
print(courses)

courses.sort()    # This will sort the list in ascending order
print(courses)

courses.sort(reverse=True)    # This will sort the list in descending order
print(courses)

sorted_courses = sorted(courses)    # This will sort the list in ascending order without altering the list
print(sorted_courses)

nums = [1, 5, 2, 4, 3]
print(min(nums))    # This will print the minimum number in the list
print(max(nums))    # This will print the maximum number in the list
print(sum(nums))    # This will print the sum of the numbers in the list

print(courses.index('Art'))    # This will print the index of 'Art' in the list
print('Art' in courses)    # This will print True because 'Art' is in the list

for course in courses:
    print(course)

for index, course in enumerate(courses):
    print(index, course)

for index, course in enumerate(courses, start=1):
    print(index, course)

course_str = ', '.join(courses)    # This will join the elements of the list with ', '
print(course_str)

new_list = course_str.split(', ')    # This will split the string into a list
print(new_list)


# mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)
list_1[0]   = 'Art'
print(list_1)
print(list_2)

# immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)

tuple_1[0] = 'Art'    # This will throw an error because tuples are immutable
print(tuple_1)
print(tuple_2)


# Sets
cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}  # This is a set
# sets do not have order, set throw away duplicates
print(cs_courses)
print('Math' in cs_courses) # Set are optimize for this

art_courses = {'History', 'Math', 'Art', 'Design'}
print(cs_courses.intersection(art_courses))    # This will print the intersection of the two sets
print(cs_courses.difference(art_courses))    # This will print the difference between the two sets
print(cs_courses.union(art_courses))    # This will print the union of the two sets


list_3 = [1, 3, 5, 7, 9, 1, 3, 5, 7, 9]
list_4 = [2, 5, 7, 7, 3, 5]
print(list_3.intersection(list_4))     # This will throw an error because lists do not have the method 'intersection'
print(set(list_3).intersection(list_4))    # This will print the intersection of the two lists
print(set(list_3).difference(list_4))    # This will print the difference between the two lists


# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {}    # This will create a dictionary
empty_set = set()    # This will create an empty set

