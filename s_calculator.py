print("ENTER THE TWO NUMBERS")

x = float(input("Enter the value for x : "))
y = float(input("Enter the value for y : "))

print("Please select operation -\n" + 
        "1. Add\n" +
        "2. Subtract\n" + 
        "3. Multiply\n" +
        "4. Divide\n") 
  
choice = input("ENTER THE CHOICE : ")

if choice == '1':
    print(x+y)

elif choice == '2':
    print(x-y)
    
elif choice == '3':
    print(x*y)
    
elif choice == '4':
    print(x/y)

else:
    print("invalid choice")
