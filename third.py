# Unpacking
"""
coordinates = (1,2,3)
x, y, z =coordinates
print(x)
"""


# Dictionary
"""
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
print(customer.get("burthdate","not available"))
customer["name"] = "Jack Smith"
print(customer.get("name"))
"""

"""
phone = input("Phone: ")
int(phone)
numbers = {
    0: "zero",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
}
output = ""
for digit in phone:
    digit = int(digit)
    output += numbers.get(digit, "!")
    output += " "
print(output)
"""

# Emoji converter
message = input(">")
words = message.split(' ')

emoji = {
    ":)": "🙂",
    ":(": "😞"
}
output = ""
for word in words:
    output += emoji.get(word, word) + " "
print(output)
