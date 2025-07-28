a = int(input("Enter your age: "))

# If statement No.1
if(a%2 == 0):
    print("You have entered an even number.")
    
# If statement No.2
if(a>=18):
    print("You are an adult.")
    
elif(a<0):
    print("Invalid age entered.") 
        
elif(a==0):
    print("You are entering zero which is not a valid age.")     
       
else:
    print("You are a minor.")    
    
print("Thank you for using the age checker!")  