"""
Test the taxi class, starting off with new taxi
"""

from Prac_08.taxi import Taxi


# Taxi.name = "Prius1"
# Taxi.fuel = 100
# Taxi.price = 1.23


def main():
    taxi = Taxi('prius1', 100)
    taxi.drive(40)
    print(taxi)
    taxi.start_fare()
    taxi.drive(100)
    print(taxi)


main()
