# WHILE Loop
"""
i = 1
while i <= 5:
    i = i + 1
print(i)
"""

"""
x = 0
y = 0
z = int(input("Star row count: "))
while x <= z:
    while y < x:
        y += 1
        print('*'*y)
    x += 1
"""

"""
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You Won!")
        break
else:
    print("sorry, you failed")
"""

"""
help_word = "help"
start_word = "car started... ready to go"
stop_word = "car stopped"
quit_word = "The end"

x = False
while not x:
    get_input = input('ENTER')
    if get_input == 'help':
        print('start - to start the car\n'
              'stop - to stop the car\n'
              'quit - to exit')
    elif get_input == 'start':
        print(start_word)
    elif get_input == 'stop':
        print(stop_word)
    elif get_input == 'quit':
        print(quit_word)
        x = True
    else:
        print('I do not understand')
"""

# FOR Loop
"""
for item in 'Python':
    print(item)
"""
"""
for item in ['yasiru', 'shehan', 'upul']:
    print(item)
"""
"""
for item in range(10):
    print(item)
"""
"""
for item in range(5,10):
    print(item)
"""

"""
for item in range(5, 10, 2):
    print(item)
"""
"""
prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f"Total: {total}")
"""

# Nested for loops
"""
for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')
"""
"""
numbers = [5, 2, 5, 2, 2]
for number in numbers:
    output = ''
    for y_count in range(number):
        output += 'x'
    print(output)
"""

"""
names = ['John', 'bob', 'mosh', 'sarah', 'mary']
print(names[0])
print(names[0:3])
"""
"""
numbers = [3, 6, 2, 8, 4, 10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)
"""

"""
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][1])

for row in matrix:
    for item in row:
        print(item)
"""

"""
numbers = [5, 2, 1, 7, 4]
numbers2 = numbers.copy()
numbers.append(20)
print(numbers)
print(2 in numbers)
numbers.sort()
print(numbers)
print(numbers2)
"""

