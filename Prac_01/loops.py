# Part a) Count in 2 from 0-20
for i in range(0, 21, 2):
    print(i, end=' ')
print()
# Part b) Count in 10 from 0-100
for i in range(0, 101, 10):
    print(i, end=' ')
print()
# Part c) Count down in 1 from 20-0
for i in range(20, 0, -1):
    print(i, end=' ')
print()
# Part d) Print number of stars
number_of_stars = int(input("How many stars: "))
for i in range(number_of_stars):
    print('*', end='')
print()
# Part e) Print number of lines
for i in range(number_of_stars + 1):
    print('*' * i)
print()
