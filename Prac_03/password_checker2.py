MIN_LENGTH = 3


# password_length = len(password)

# First version of password checker
def program_1():
    password = input("Enter a password of at least 3 characters: ".format(MIN_LENGTH))
    while len(password) < MIN_LENGTH:
        print("Invalid")
        password = input("Enter a password of at least 3 characters: ".format(MIN_LENGTH))
    else:
        print('*' * len(password))


program_1()


def get_password(min_length):
    password = input("Enter a password of at least 3 characters: ".format(min_length))
    while len(password) < min_length:
        print("Invalid")
        password = input("Enter a password of at least 3 characters: ".format(min_length))
    return password


def print_asterisks(sequence):
    print('*' * len(sequence))


def main():
    password = get_password(MIN_LENGTH)
    print_asterisks(password)

main()