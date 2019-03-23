# 1
output_file = "name.txt"
output_file = open("name.txt", "w")
user_name = input("Enter your name: ")
print(user_name, file=output_file)

# Close the file
output_file.close()

# 2
input_file = open("name.txt", 'r')
user_name = input_file.read()
print("Your name is", user_name)

# 3
input_file = "numbers.txt"
input_file = open("numbers.txt", "r")
number1 = float(input_file.readline())
number2 = float(input_file.readline())
input_file.close()
print("Addition of (2) numbers:", number1 + number2)

# 4(Extension)
input_file = open("numbers.txt", "r")
total = 0
for line in input_file:
    number = int(line)
    total += number
# number1 = float(input_file.readline())
# number2 = float(input_file.readline())
input_file.close()
print("Addition of (all) numbers:", total)