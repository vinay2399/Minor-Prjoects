import math

def add(x, y):
   return x + y

def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
   return x / y

def modulo(x, y):
    return x % y

def Basic_cal():
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Modulo")
    print("6.Back")
    print("7.Exit")

    choice = input("Enter choice:")

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if choice == '1':
        print(num1,"+",num2,"=", add(num1,num2))

    elif choice == '2':
        print(num1,"-",num2,"=", subtract(num1,num2))

    elif choice == '3':
        print(num1,"*",num2,"=", multiply(num1,num2))

    elif choice == '4':
        print(num1,"/",num2,"=", divide(num1,num2))

    elif choice== '5':
        print(num1,"%",num2,"=",modulo(num1,num2))

    elif choice == '6':
        calculator()

    elif choice == '7':
        exit

    else:
        print("Invalid input")

def Scientific_cal():
    print("Choose one option")
    print("1.Representation Functions")
    print("2.Trignometric Functions")
    print("3.Logarithmic Functions")
    print("4.Angular Conversions")
    print("5.Exponential Functions")
    print("6.Back")
    print("7.Exit")
    key=input("")

    if key == '1':
        representation_func()

    elif key == '2':
        trignometric_func()

    elif key == '3':
        logarithmic_func()

    elif key == '4':
        angular_conversions()

    elif key == '5':
        exponential_func()

    elif key == '6':
        calculator()

    elif key == '7':
        exit

    else:
        print("Enter correct option")
        Scientific_calc()
    
        
def representation_func():
        print('Choose one option')
        print("1.ceil(x)")
        print("2.copysign(x){Return a float with the magnitude (absolute value) of x but the sign of y}")
        print("3.fabs(x){Return the absolute value of x}")
        print("4.factorial(x)")
        print("5.floor(x)")
        print("6.isinfite(x){Return True if x is neither an infinity nor a NaN, and False otherwise}")
        print("7.modf(x){Return the fractional and integer parts of x. Both results carry the sign of x and are floats}")
        print("8.trunc(x){Return the Real value x truncated to an Integral }")
        print("9.Back")
        print("10.Exit")
        key1=input('')
        x=float(input('Enter the value of x'))

        if key1 == '1':
            print('ceil(',x,')=',math.ceil(x))

        elif key1 == '2':
            print('copysign(',x,')=',math.copysign(x))

        elif key1 == '3':
            print('fabs(',x,')=',math.fabs(x))

        elif key1 == '4':
            print('factorial(',x,')=',math.factorial(x))

        elif key1 == '5':
            print('floor(',x,')=',math.floor(x))

        elif key1 == '6':
            print('isinfinite(',x,')=',math.isinfinite(x))

        elif key1 == '7':
            print('modf(',x,')=',math.modf(x))

        elif key1 == '8':
            print('trunc(',x,')=',math.trunc(x))

        elif key1 == '9':
            Scientific_cal()


        elif key1 == '10':
            exit

        else:
            print('Please enter correct option')
            representation_func()

def trignometric_func():
        print("Choose one option")
        print("1.Sin(x)")
        print("2.Cos(x)")
        print("3.Tan(x)")
        print("4.aSin(x)")
        print("5.aCos(x)")
        print("6.aTan(x)")
        print("7.Back")
        print("8.Exit")
        key1=input('')
        
        x=int(input("Enter the value of x"))
        if key1 == '1':
              print('Sin(',x,')=',math.sin(x))

        elif key1 == '2':
              print('Cos(',x,')=',math.cos(x))

        elif key1 == '3':
             print('Tan(',x,')=',math.tan(x))

        elif key1 == '4':
             print('aSin(',x,')=',math.asin(x))

        elif key1 == '5':
             print('aCos(',x,')=',math.acos(x))

        elif key1 == '6':
             print('aTan(',x,')=',math.atan(x))

        elif key1 == '7':
              Scientific_cal()

        elif key1 == '8':
              exit


        else:
              print("please enter correct option")
              trignometric_func()

def logarithmic_func():
        print("Choose one option")
        print("1.log(x,base)")
        print("2.log1p(x)")
        print("3.log2(x)")
        print("4.log10(x)")
        print("5.Back")
        print("6.Exit")
        key1=input('')
        x=int(input("Enter the value of x"))
        if key1 == '1':
            base=int(input('Enter the base'))
            print('log(',x,',',base,')=',math.log(x,base))

        elif key1 == '2':
            print('log1p(',x,')=',math.log1p(x))

        elif key1 == '3':
            print('log2(',x,')=',math.log2(x))

        elif key1 == '4':
            print('log10(',x,')=',math.log10(x))

        elif key1 == '5':
              Scientific_cal()

        elif key1 == '6':
              exit

        else:
              print('Please enter correct option')
              exponential_func()

def angular_conversions():
            print("Choose one option")
            print("1.degrees(x)")
            print("2.radians(x)")
            print("3.Back")
            print("4.Exit")
            key1=input('')
            x=float(input('Enter the value of x'))
            if key1 == '1':
                    print('degrees(',x,')=',math.degrees(x))

            elif key1 == '2':
                    print('radians(',x,')=',math.radians(x))

            elif key1 == '3':
                    Scientific_cal()

            elif key1 == '4':
                    exit

            else:
              print('Please enter correct option')
              angular_conversions()

def exponential_func():
            print("Choose one option")
            print("1.exp(x)")
            print("2.expm1(x)")
            print("3.pow(x,y)")
            print("4.sqrt(x)")
            print("5.Back")
            print("6.Exit")
            key1=input('')
            x=int(input('Enter the value of x'))

            if key1 == '1':
                    print('exp(',x,')=',math.exp(x))

            elif key1 == '2':
                    print('expm1(',x,')=',math.expm1(x))

            elif key1 == '3':
                    y=int(input('Enter the value of y'))
                    print('pow(',x,',',y,')=',math.expm1(x))

            elif key1 == '4':
                    print('expm1(',x,')=',math.expm1(x))

            elif key1 == '5':
                    Scientific_cal()

            elif key1 == '6':
                    exit

            else:
              print('Please enter correct option')
              exponential_func()
def calculator():
    print("Choose one option")
    print("1.Basic Calculator")
    print("2.Scientific Calculator")
    print("3.Exit")
    num=input('')

    if num == '1':
        Basic_cal()

    elif num == '2':
        Scientific_cal()

    elif num == '3':
        exit

    else:
        print("Please enter correct option")
        calculator()

calculator()
                    


                    

                    
              
                    


    



   
