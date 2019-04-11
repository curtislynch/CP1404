"""
CP1404/CP5632 Practical
State names in a dictionary
"""

COLOUR_NAMES = {"AliceBlue": "#f08ff", "AquaMarine2": "#7fffd4", "Blue1": "#0000ff",
                "Brown2": "#ee3b3b", "CadetBlue": "#5f9ea0", "Chartreuse1": "#7fff00",
                "Chocolate": "#d2691e", "Coral": "#ff7f50", "Cyan1": "#00ffff", "DarkSeaGreen": "#8fbc8f"}
# print(STATE_NAMES)

colour = input("Enter colour name: ")
while colour != "":
    if colour in COLOUR_NAMES:
        print("The colour code for, {}, is {}".format(colour, COLOUR_NAMES.get(colour)))
    else:
        print("Invalid colour")
    colour = input("Enter colour name: ")
