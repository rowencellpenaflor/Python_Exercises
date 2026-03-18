menu = input("Enter menu choice (lunch or dinner): ")
meal = int(input("Choose between 1-3: "))

if menu == "lunch":
	if meal == 1:
		print("Caesar salad")
	elif meal == 2:
		print("Spicy chicken wrap")
	elif meal == 3:
		print("Butternut squash soup")
	else:
		print("Invalid choice")

elif menu == "dinner":
	if meal == 1:
		print("Baked Salmon")
	elif meal == 2: 
		print("Turkey burger")
	elif meal == 3:
		print("Mushroom Risotto")
	else:
		print("Invalid choice")

else:
	print("Invalid choice")
		