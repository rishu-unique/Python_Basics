s = {1, 4, 34, 56, 6, 4, 4, "Alen"} # Numbers and strings in sets

print(s, type(s)) # Output: {1, 34, 4, 6, 56, 'Alen'} In random order
# Note: Sets can contain mixed data types, but all elements must be hashable.

s.add(423)
print(s, type(s)) # Output: {1, 34, 4, 6, 56, 'Alen', 423} In random order

s.remove(4) 
print(s, type(s)) # Output: {1, 34, 6, 56, 'Alen', 423} In random order