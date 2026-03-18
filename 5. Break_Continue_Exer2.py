my_list = [1, 5, 7, 12, 5, 17, 9, 2, 4]

total = 0

for i in my_list:
    if i < 5:
        # TO DO: numbers less than 5 should be skipped.
        continue
    else: 
        # TO DO: numbers greater than 5 should be summed up.
        total += i
print(total)