# Writing to and reading from a file
with open("stats.txt", "w") as f:
    f.write("Player: Jett\nKills: 20")

with open("stats.txt", "r") as f:
    content = f.read()
    print(content)