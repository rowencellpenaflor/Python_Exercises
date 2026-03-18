"""

Sum of odd numbers
"""

n1 = int(input("Enter an integer: "))
n2 = int(input("Enter another integer: "))

number = n1
total = 0

while number <= n2:

    if number % 2 != 0:
        print(number)
        total += number
    
    number += 1

print(f"The sum of all odd numbers between {n1} and {n2} is {total}") 