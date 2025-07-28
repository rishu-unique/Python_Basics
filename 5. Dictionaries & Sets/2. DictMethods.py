
marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    0: "David",
}

print(marks.items())  # Output: dict_items([('Alice', 85), ('Bob', 92), ('Charlie', 78), (0, 'David')])
print(marks.keys())   # Output: dict_keys(['Alice', 'Bob', 'Charlie', 0])
print(marks.values()) # Output: dict_values([85, 92, 78, 'David'])

marks.update({"Alice": 90})  # Update Alice's score
marks.update({"Alen": 88})  # Add a new entry for Alen
print(marks)  # Output: {'Alice': 90, 'Bob': 92, 'Charlie': 78, 0: 'David'}

print(marks.get("Alice"))  # Output: 90 Prints none if key not found
print(marks["Alice"])   # Output: 90 Prints error if key not found 
marks.clear()  # Clear all entries in the dictionary
print(marks)  # Output: {}