"""
Guitar Program for user input
"""

from Prac_06.guitar import Guitar


def main():
    """Blah"""
    guitars = []

    print("My Guitars!")

    name = input("What is your Guitar Name? ")
    # print(user_name)
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    """
    Loop to run program when user enters valid name
    """

    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(new_guitar, "Added")
        name = input("What is your Guitar Name? ")
        print("These are my Guitars: ")

        for i, guitar in enumerate(guitars):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = "(Vintage)"
            print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                                      vintage_string))


main()
