
"""
Terms and conditions prompt

Write a function, terms(), that asks the user to accept the terms and conditions, 
reads in Y/N, and outputs a response. In the main program, read in the 
number of users and call terms() for each user.

"""
def terms():
    choice = input("Do you accept the terms and conditions?")
    if choice == "Y":
        accepted()
    elif choice == "N":
        rejected()

def accepted():
    print("Thank you for accepting the terms.")

def rejected():
    print("You have rejected the terms. Thank you.")


times = int(input("Enter input/s: "))

i = 1
while i <= times:
    terms()
    i += 1
