"""
Estimated days alive
Write a function, days_alive(), that takes in an age in years and outputs the estimated days the user has been alive as an integer. 
Assume each year has 365.24 days.
"""

def days_alive(age):
	days = round(age * 365.24)
	return days

alive = int(input("Enter your age: "))
day = days_alive(alive)
print(f"You have been alive for about {day} days.")