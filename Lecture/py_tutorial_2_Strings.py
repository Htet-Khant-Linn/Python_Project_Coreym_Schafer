message = """Hello World!"""    # This is a string
print(message)
print(len(message))    # This will print the length of the string
print(message[0])    # This will print the first character of the string
# print(message[12])    # This will throw an error because the index is out of range
print(message[0:5])    # This will print the first 5 characters of the string
print(message[6:])    # This will print the string from the 7th character to the end
print(message.lower())    # This will print the string in lower case
print(message.upper())    # This will print the string in upper case
print(message.count("Hello"))    # This will print the number of times "Hello" appears in the string
print(message.count("l"))    # This will print the number of times "l" appears in the string
print(message.count("l", 0, 5))    # This will print the number of times "l" appears in the string from index 0 to 4
print(message.find("World"))    # This will print the index of "World" in the string
print(message.find("Universe"))    # This will print -1 because "Universe" is not in the string
new_message = message.replace("World", "Universe")    # This will replace "World" with "Universe"
print(new_message)

greeting = "Hello"
name = "Michael"

message = greeting + ', ' + name + '. Welcome!'
print(message)

message = '{}, {}. Welcome!'.format(greeting, name)
print(message)

message = f'{greeting}, {name.upper()}. Welcome!'
print(message)

print(dir(name))
print(help(str))
# print(help(str.lower))
# print(help(str.upper))
# print(help(str.count))
# print(help(str.find))
# print(help(str.replace))
# print(help(str.format))
# print(help(str.format_map))
# print(help(str.index))
# print(help(str.isalnum))
# print(help(str.isalpha))
# print(help(str.isascii))
# print(help(str.isdecimal))
# print(help(str.isdigit))
# print(help(str.isidentifier))
# print(help(str.islower))
# print(help(str.isnumeric))
# print(help(str.isprintable))
# print(help(str.isspace))
# print(help(str.istitle))
# print(help(str.isupper))
# print(help(str.join))
# print(help(str.ljust))
# print(help(str.lower))
# print(help(str.lstrip))
# print(help(str.maketrans))
# print(help(str.partition))
# print(help(str.replace))
# print(help(str.rfind))
# print(help(str.rindex))
# print(help(str.rjust))
# print(help(str.rpartition))
# print(help(str.rsplit))
# print(help(str.rstrip))
# print(help(str.split))
# print(help(str.splitlines))
# print(help(str.startswith))
# print(help(str.strip))
# print(help(str.swapcase))
# print(help(str.title))
# print(help(str.translate))
# print(help(str.upper))
# print(help(str.zfill))
# print(help(str.casefold))
# print(help(str.center))
# print(help(str.encode))
# print(help(str.expandtabs))
# print(help(str.format))
# print(help(str.format_map))
# print(help(str.index))
# print(help(str.isalnum))
# print(help(str.isalpha))
# print(help(str.isascii))
# print(help(str.isdecimal))
# print(help(str.isdigit))
# print(help(str.isidentifier))
# print(help(str.islower))
# print(help(str.isnumeric))
# print(help(str.isprintable))
# print(help(str.isspace))
# print(help(str.istitle))
# print(help(str.isupper))
# print(help(str.join))
# print(help(str.ljust))
# print(help(str.lower))
# print(help(str.lstrip))
# print(help(str.maketrans))
# print(help(str.partition))
# print(help(str.replace))
# print(help(str.rfind))
# print(help(str.rindex))
# print(help(str.rjust))
# print(help(str.rpartition))
# print(help(str.rsplit))
# print(help(str.rstrip))
# print(help(str.split))
# print(help(str.splitlines))
# print(help(str.startswith))
# print(help(str.strip))
# print(help(str.swapcase))
# print(help(str.title))