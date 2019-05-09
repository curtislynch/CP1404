"""
Use this program to run class operation
"""

from Prac_06.guitar import Guitar


def testing():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    main = Guitar(name, year, cost)
    another = Guitar("Another Guitar", 2012, 1512.9)

    """
    From these guitars test functions with print functions (same as given output)
    """

    print("{} get_age() - Expected {}. Got {}".format(main.name, 97, main.get_age()))

    print("{} get_age() - Expected {}. Got {}".format(another.name, 7, another.get_age()))

    print("{} is_vintage() - Expected {}. Got {}".format(main.name, True, main.is_vintage()))

    print("{} is_vintage() - Expected {}. Got {}".format(another.name, False, another.is_vintage()))


if __name__ == '__main__':
    testing()
