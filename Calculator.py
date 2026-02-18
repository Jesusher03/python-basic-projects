#Comments: This is my first program, this is my calculator version 1.0
#Developer: Jesus Hernandez
#Date: 16-Feb-2026


print('Calculator')

result = 0.0

answer = input("options \na) Addition \nb) Subtraction \nc) Multiplication \nd) Division \n")

if answer in("a","b","c","d"):
    num1 = float(input("Select number for num1"))
    num2 = float(input("Select a  number for num2"))  

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