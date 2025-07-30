# If-Else ladder to determine player's performance
score = int(input("Enter your game score: "))

if score >= 90:
    print("Excellent performance!")
elif score >= 70:
    print("Good job!")
elif score >= 50:
    print("Decent, keep improving!")
else:
    print("Try harder next time!")