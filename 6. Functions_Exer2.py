"""
Terms and conditions prompt
Write a function, terms(), that asks the user to accept the terms and conditions, 
reads in Y/N, and outputs a response. In the main program, read in the number of 
users and call terms() for each user.
"""

def terms():
    term = input("Do you accept the terms and conditions?\n")
    if term == "Y":
        print("Thank you for accepting.")
    elif term == "N":
        print("Have a good day.")

num = int(input("Enter number of users: "))

for i  in range(num):
    terms()