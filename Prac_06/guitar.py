"""
Write the Guitar Class, to store fields about Guitars
"""


class Guitar:
    """
    Define name, year and cost for each guitar in an init, set string to blank and values to 0
    """

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${}".format(self.name, self.year, self.cost)

    def get_age(self):
        return 2019 - self.year

    def is_vintage(self):
        return self.get_age() >= 50
