# Spam Detection Program
# This program checks if a message contains spam keywords
p1 = "Make a lot of money"
p2 = "by now"
p3 = "sbscribe this"
p4 = "click this"

message = input("Enter the message: ")

if (p1 in message or p2 in message or p3 in message or p4 in message):
    print("This is a spam message")
    
else:
    print("This is not a spam message")
    