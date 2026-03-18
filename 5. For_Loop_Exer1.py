"""
Counting spaces
Write a program using a for loop that takes in a string as input 
and counts the number of spaces in the provided string. 
"""


usr_in = input()

count = 0
for c in usr_in:
    if c == ' ':
        count += 1
        
print(count)