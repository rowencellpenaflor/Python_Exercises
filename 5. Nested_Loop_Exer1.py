"""
Printing a triangle of numbers
"""
# Descending 
for n in range(10, 1, -1):
    i = 1
    while i < n:
        print (i, end = " ")
        i += 1
    print()

# Ascending 
for n in range(1, 10):
    i = 1
    while i <= n:
        print (i, end = " ")
        i += 1
    print()