"""
Write a program that takes in a positive integer number (N) 
and prints out the first N prime numbers on separate lines.
"""

N = int(input("Enter number: "))

while N <=0:
    print("Enter only positive integers....")
    N = int(input("Enter number again: "))
    
n = N*2 + 1 
for num in range(1, n+1):
	if num > 1:
		for i in range(2, num):
			if num % i == 0:
				break
		else:
			print(num)

            
# Additional: Checking if a number is prime or not

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
