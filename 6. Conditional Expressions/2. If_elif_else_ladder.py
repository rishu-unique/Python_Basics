a = int(input("Enter your age: "))

# If elif else ladder to check age category

if(a>=18):
    print("You are an adult.")
    
elif(a<0):
    print("Invalid age entered.") 
        
elif(a==0):
    print("You are entering zero which is not a valid age.")     
       
else:
    print("You are a minor.")    
    
print("Thank you for using the age checker!")     