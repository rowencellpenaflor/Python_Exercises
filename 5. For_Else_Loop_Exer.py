list1 =  [11, 13, 10, 15]
list2 = [1, 3, 10, 5]

total = 0

# TO DO: add the value of integer i to total if i < 10
for i in list1:
    if i < 10:
        total += i
    else:
        break
else:
    print("The sum of all the integers are", total)


