file=open("inventory.txt", "a")
while True:
	newitem=input("Enter new inventory item: ")
	if newitem == "exit":
		print("All done!")
		break
	file.write(newitem + "\n")
file.close
