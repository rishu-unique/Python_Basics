name= "People are weird  as hell"

print(name.find("  "))  # This will return the index of the first occurrence of a space
print(name.find("weird"))  # This will return the index of the first occurrence of "weird"

print(name.replace("  "," "))  # This will replace double spaces with a single space
print(name.replace("weird", "strange"))  # This will replace "weird" with "strange"

print(name) # The original string remains unchanged
