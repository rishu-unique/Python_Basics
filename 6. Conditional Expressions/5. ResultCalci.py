# Result: Check if a student has passed or failed based on marks
# Input: Marks in three subjects
marks1 = int(input("Enter marks 1:"))
marks2 = int(input("Enter marks 2:"))
marks3 = int(input("Enter marks 3:"))

#Check for total percentage
total_percentage = (100*(marks1 + marks2 + marks3)) / 300 

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You have passed the exam: ", total_percentage)
    
else:
    print("You have failed the exam: ", total_percentage)    