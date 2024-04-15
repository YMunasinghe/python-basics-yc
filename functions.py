"""
def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')


print("Start")
greet_user("Munasinghe", 'Yasiru')
print("finish")
"""

"""

def square(number):
    result = number * number
    # return result


print(square(3))
"""

"""
def emojis(inputs):
    inputs = get_input.split(' ')
    emoji = {
        ":)": "🙂",
        ":(": "😞"
    }
    output = ""
    for input1 in inputs:
        output += emoji.get(input1, input1) + " "
    return output

get_input = input("> ")
print(emojis(get_input))
"""

"""
try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(risk)
except ZeroDivisionError:
    print('Age can not be 0')
except ValueError:
    print('Invalid Value ')
"""

try:
    monthIncome = int(input("Input month income "))
    yearIncome = monthIncome * 12
    print(yearIncome)
except ZeroDivisionError:
    print('Value can not br zero')
except ValueError:
    print('Invalid input')
