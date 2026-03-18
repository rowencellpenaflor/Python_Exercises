"""
Printing two triangles

"""

strings = ["*", "+"]

for n in strings:
    i = 4
    while i >= 1:
        print (n * i , end = " ")
        i -= 1
        print()

