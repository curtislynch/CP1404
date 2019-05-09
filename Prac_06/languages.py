"""
Import Programming Language class into this program
"""

from Prac_06.programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [ruby, python, visual_basic]
    print("Dynamically Typed Languages:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
