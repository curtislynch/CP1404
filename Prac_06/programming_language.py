"""
Making a simple class for a programming language
Information from Programming Language Comparision Page
"""


class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return "{}, {} typing, Reflection = {}, First appeared in 1991".format(self.name, self.typing, self.reflection,
                                                                               self.year)

    def is_dynamic(self):
        return self.typing == "Dynamic"

