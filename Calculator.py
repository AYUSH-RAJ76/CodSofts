def add(num1, num2):
    return num1+num2

def sub(num1, num2):
    return num1-num2

def multiply(num1, num2):
    return num1*num2

def divide(num1, num2):
    if num2 == 0:
        return "Error ! Division by Zero. "
    else:
        return num1/num2
    
while True:


    print(
        """ MENU 
   
     Enter The Operators.
    1 Enter "+" For Addition.
    2 Enter "-" For Subtraction.
    3 Enter "*" For Multiplication.
    4 Enter "/" For Divison.

   Enter "0" For Exit.

   THANK YOU!!
    """
    )

    choice = input("Enter Choice (1,2,3,4,0) : ")
    
    if choice == 0:
        print("Exiting The calculator .\n    Thanku you!")
        break

    if choice in ['1','2','3','4']:
        num1 = float(input("Enter first number:"))
        num2 = float(input("Enter second number:"))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}\n") 

        elif choice == '2':
            print(f"{num1} - {num2} = {sub(num1,num2)}")

        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1,num2)}")
        
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1,num2)}")

    else:
        print("Invalid input ,Please enter a valid choice.")