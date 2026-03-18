usr = input("Enter string: ")

# Printing the given input
print("You have entered", usr)

#TO DO: identify if the string contains a space character
for n in usr:
    if n == " ":
        statement = "Found"
        break
    statement = "Not Found"

print(statement)
    