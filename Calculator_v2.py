#Comments: This is my first program, this is my calculator version 2.0
#Developer: Jesus Hernandez
#Date: 18-Feb-2026


print('Calculator')

result = 0.0
ans ="yes"
while ans == "yes":
    answer = input("options \na) Addition \nb) Subtraction \nc) Multiplication \nd) Division \n").lower().strip()

    if answer in ("a","b","c","d"):
        while True:
            try:
                num1 = float(input("Select number for num1"))
                break
            except ValueError:
                print("Invalid input. please enter a number")
                
        while True:
            try:
                num2 = float(input("Select a  number for num2"))
                break
            except ValueError:
                print("Invalid input. please enter a number")
           
        if answer == 'a':
            print("Addition (+)")
            result = num1 + num2
            
        elif answer == "b":
            print("subtraction (-)")
            result = num1 - num2
            
        elif answer == "c":
            print("Multiplication (*)")
            result = num1 * num2
            
        elif answer == "d":
            print("Division (/)")
            if num2 == 0:
                result = 'Error: Division by zero is not allowed'
            else:
                result = num1 / num2

        print('This is your result: ', result)

    else:
        print("This isn't an option")
        
    ans = input("You what to continue? \nYes/No").lower().strip()
    
    while ans != "yes" and ans != "no":
        ans = input("please type Yes or No").lower().strip()
    
        
print("See you next time")
