"""
Printing even and odd integers on given range 
"""

n1 = int(input("Enter an integer: "))
n2 = int(input("Enter another integer larger than the first one: "))


if n1 >= n2:
    print("Value Error...") 

else:
    # Printing even numbers in increasing order (inclusive)
    for num in range(n1, n2 + 1, 2):
        print(num, end = " ")
    
    print("")
    
    # Printing odd numbers in decreasing order (exclusive)
    for num in range(n2 - 1, n1, -2):
        print(num, end = " ")