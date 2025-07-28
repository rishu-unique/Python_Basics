friends = ['Alice', 'Bob', 'Charlie', 'David',5,345.2,False]

print(friends)

friends.append( 'Eve')  # Adding a new element to the end of the list

print(friends)  # Output: ['Alice', 'Bob', 'Charlie', 'David', 5, 345.2, False, 'Eve']

l1 = [1,4,64,12,13]
l1.sort()  # Sorting the list in ascending order
print(l1)  # Output: [1, 4, 12, 13, 64]

l1.reverse()  # Reversing the list
print(l1)  # Output: [64, 13, 12, 4, 1]

l1.insert(4,2)  # Inserting 2 at index 4 (will be added at the end)
print(l1)  # Output: [64, 13, 12, 4, 2, 1]

l1.pop(3)  # Removing the element at index 3
print(l1)  # Output: [64, 13, 12, 2, 1]

l1.remove(64)  # Removing the first occurrence of 64
print(l1)  # Output: [13, 12, 2, 1]