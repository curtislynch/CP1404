"""Creating a list for users numbers"""

# Start with empty list
numbers = []

for i in range(5):
    user_number = int(input("Number: "))
    numbers.append(user_number)
print("The first number is: ", numbers[0])
print("The last number is: ", numbers[4])
print("The smallest number is: ", min(numbers))
print("The largest number is: ", max(numbers))
print("The average is: ", sum(numbers) / len(numbers))


# Start of Woefully inadequate security checker

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
