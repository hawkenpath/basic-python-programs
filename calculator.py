def addNumbers():
    welcomeAdd = "This is the Add Section"
    print(welcomeAdd)
    firstNumber = int(input("Input the first number to add"))
    secondNumber = int(input("Input the Second number to add"))
    moreNumberInputs = input("Would you like to add more numbers?")
    moreNumberInputs = moreNumberInputs.lower()
    if moreNumberInputs =="yes":
            thirdNumber = int(input("Input the Third number"))
            changeOperator =input("Would you like to times,add,subtract or divide this number?")
            changeOperator.lower()
            if changeOperator =="add":
                print(firstNumber, "+", secondNumber, "+", thirdNumber, "=", firstNumber + secondNumber + thirdNumber)
            elif changeOperator =="subtract":
                 print(firstNumber, "+", secondNumber, "-", thirdNumber, "=", firstNumber + secondNumber - thirdNumber)
            elif changeOperator =="times":
                 print(firstNumber, "+", secondNumber, "x", thirdNumber, "=", secondNumber * thirdNumber + firstNumber)
            elif changeOperator =="divide":
                 print(firstNumber, "+", secondNumber, "+", thirdNumber, "=", secondNumber / thirdNumber + firstNumber)
            elif changeOperator:
                error = "Error 3: No operator deteccted, running sum with addition operator rerun the command to change the operator"
                print(error)
                print(firstNumber, "+", secondNumber, "+", thirdNumber, "=", firstNumber + secondNumber + thirdNumber)
               
                
                
                
            
    elif moreNumberInputs =="no":
        print(firstNumber, "+", secondNumber, "=", firstNumber+secondNumber)
    elif moreNumberInputs:
        error = "Error 2: No Recognized statement detected, running sum with previously stated numbers"
        print(error)
        print(firstNumber, "+", secondNumber, "=", firstNumber+secondNumber,)

def subtractNumbers():
    welcomeSubtract = "This is the Subtract Section"
    
    print(welcomeSubtract)
    firstNumber = int(input("Input the First Number to Subtract"))
    secondNumber = int(input("Input the Second Number to Subtract"))
    moreNumberInputs = input("Would you like to add more numbers?")
    moreNumberInputs = moreNumberInputs.lower()
    if moreNumberInputs =="yes":
            thirdNumber = int(input("Input the Third Number"))
            changeOperator =input("Would you like to times,add,subtract or divide this number?")
            changeOperator.lower()
            if changeOperator =="add":
                 print(firstNumber, "-", secondNumber, "+", thirdNumber, "=", firstNumber - secondNumber + thirdNumber)
            elif changeOperator =="subtract":
                 print(firstNumber, "-", secondNumber, "-", thirdNumber, "=", firstNumber - secondNumber - thirdNumber)
            elif changeOperator =="times":
                 print(firstNumber, "-", secondNumber, "x", thirdNumber, "=", secondNumber * thirdNumber - firstNumber)
            elif changeOperator =="divide":
                 print(firstNumber, "-", secondNumber, "+", thirdNumber, "=", secondNumber / thirdNumber - firstNumber)
            elif changeOperator:
                error = "Error 3: No operator deteccted, running sum with subtraction operator rerun the command to change the operator"
                print(error)
                print(firstNumber, "-", secondNumber, "-", thirdNumber, "=", firstNumber - secondNumber - thirdNumber)
                
            
    elif moreNumberInputs =="no":
        print(firstNumber, "-", secondNumber, "=", firstNumber-secondNumber)
    elif moreNumberInputs:
        error = "Error 2: No Recognized statement detected, running sum with previously stated numbers"
        print(error)
        print(firstNumber, "-", secondNumber, "=", firstNumber-secondNumber,)
        
def divideNumbers():
    welcomeDivide = "This is the Divide Section"
    print(welcomeDivide)
    firstNumber = int(input("Input the First Number to Divide"))
    secondNumber = int(input("Input the Second Number to Divide"))
    moreNumberInputs = input("Would you like to add more numbers?")
    moreNumberInputs = moreNumberInputs.lower()
    if moreNumberInputs =="yes":
            thirdNumber = int(input("Input the Third Number"))
            changeOperator=input("Would you like to times,add,subtract or divide this number")
            changeOperator.lower()
            if changeOperator == "add":
                print(firstNumber, "/", secondNumber, "+", thirdNumber, "=", firstNumber / secondNumber + thirdNumber)
            elif changeOperator =="subtract":
                 print(firstNumber, "/", secondNumber, "-", thirdNumber, "=", firstNumber / secondNumber - thirdNumber)
            elif changeOperator =="times":
                 print(firstNumber, "/", secondNumber, "x", thirdNumber, "=", secondNumber * thirdNumber / firstNumber)
            elif changeOperator =="divide":
                 print(firstNumber, "/", secondNumber, "/", thirdNumber, "=", secondNumber / thirdNumber / firstNumber)
            elif changeOperator:
                error = "Error 3: No operator deteccted, running sum with division operator rerun the command to change the operator"
                print(error)
                print(firstNumber, "-", secondNumber, "-", thirdNumber, "=", firstNumber - secondNumber - thirdNumber)
            
    elif moreNumberInputs =="no":
        print(firstNumber, "/", secondNumber, "=", firstNumber/secondNumber)
    elif moreNumberInputs:
        error = "Error 2: No Recognized statement detected, running sum with previously stated numbers"
        print(error)
        print(firstNumber, "/", secondNumber, "=", firstNumber/secondNumber,)

def multiplyNumbers():
    welcomeTimes = "This is the Multiply Section"
    print(welcomeTimes)
    firstNumber = int(input("Input the First Number to Multiply"))
    secondNumber = int(input("Input the Second Number to Multiply"))
    moreNumberInputs = input("Would you like to add more numbers?")
    moreNumberInputs = moreNumberInputs.lower()
    if moreNumberInputs =="yes":
            thirdNumber = int(input("Input the Third Number"))
            changeOperator=input("Would you like to times,add,subtract or divide this number")
            changeOperator.lower()
            if changeOperator == "add":
                print(firstNumber, "x", secondNumber, "+", thirdNumber, "=", firstNumber * secondNumber + thirdNumber)
            elif changeOperator =="subtract":
                 print(firstNumber, "x", secondNumber, "-", thirdNumber, "=", firstNumber / secondNumber * thirdNumber)
            elif changeOperator =="times":
                 print(firstNumber, "x", secondNumber, "x", thirdNumber, "=", secondNumber * thirdNumber * firstNumber)
            elif changeOperator =="divide":
                 print(firstNumber, "x", secondNumber, "/", thirdNumber, "=", secondNumber / thirdNumber * firstNumber)
            elif changeOperator:
                error = "Error 3: No operator deteccted, running sum with multiplication operator rerun the command to change the operator"
                print(error)
                print(firstNumber, "-", secondNumber, "-", thirdNumber, "=", firstNumber - secondNumber - thirdNumber)
            
    elif moreNumberInputs =="no":
        print(firstNumber, "x", secondNumber, "=", firstNumber*secondNumber)
    elif moreNumberInputs:
        error = "Error 2: No Recognized statement detected, running sum with previously stated numbers"
        print(error)
        print(firstNumber, "x", secondNumber, "=", firstNumber*secondNumber,)

def welcome():
    welcomeToProgram = "Welcome to my basic calculator program, you can use up to three numbers for each method"
    print(welcomeToProgram)


def calculate():
    welcome()
    Calculator=input("Would you like to add subtract, divide or multiply")
    Calculator = Calculator.lower()
    if Calculator=="add":
           addNumbers()
    elif Calculator=="subtract":
            subtractNumbers()
    elif Calculator=="divide":
            divideNumbers()
    elif Calculator=="multiply":   
            multiplyNumbers()      
    else:
        print("Error 1:Method not stated, Enter the command again and try again")
            
                       
                            
                        
            
                    
 
            


        
    
         

