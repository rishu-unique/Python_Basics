# This program checks if a post contains the word "Python" in any case.
# It uses the lower() method to make the check case-insensitive.

post = input("Enter a post: ")

if("Python".lower() in post.lower()):
    print("This post is about Python!")
    
else:
    print("This post is not about Python.")
