"""
Averaging lists
Write a function, avg_list(), that takes in a list and returns the average of the list values.
"""

# Define avg_list()
def avg_list(list):
    sum = 0
    i = 0
    for num in list:
        sum += num
        i += 1
	    
    avg = sum / i
    return avg

list1 = [34, 29, 77, 30, 48, 92]
print(list1)
print(f"Avg is: {avg_list(list1):.1f}")

list2 = [4, 2, 12, 8, 8]
print(list2)
print(f"Avg is: {avg_list(list2):.1f}")