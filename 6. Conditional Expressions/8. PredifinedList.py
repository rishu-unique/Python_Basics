# This code checks if a name is in a predefined list and prints a message accordingly.
l = ["Alen", "Bob", "Charlie", "David"]

name = input("Enter a name: ")

if(name in l):
    print("Your name is in the list. ")
else:
    print("Your name is not in the list.")