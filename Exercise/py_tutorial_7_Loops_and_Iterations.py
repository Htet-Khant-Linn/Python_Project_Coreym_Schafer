nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        print('Found!')
        break   # break the loop
    print(num)  
# Output: 1 2 Found!

for num in nums:
    if num == 3:
        print('Found!')
        continue   # skip the current iteration
    print(num)
# Output: 1 2 Found! 4 5

for num in nums:
    for letter in 'abc':
        print(num, letter)  # nested loop
        
for i in range(10):
    print(i)    # 0 to 9

for i in range(1, 11):
    print(i)    # 1 to 10

x = 0

while x < 10:
    print(x)
    x += 1
    
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1
    
while True:
    if x == 5:
        break
    print(x)
    x += 1
# to interrupt continuous loop, press Ctrl + C


