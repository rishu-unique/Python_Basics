# Handling division error
try:
    x = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")