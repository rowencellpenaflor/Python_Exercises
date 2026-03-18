"""
Reading inputs in a while loop
"""

string = input("Enter word: ")

while string != "begin":
    print("Wrong input! Try again...")
    string = input("Enter word: ")
print("The while loop condition has been met.")