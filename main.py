def add(num1,num2):
    if type(num1) is int or type(num1) is float and type(num2) is int or type(num2) is float:
        print(num1+num2)
    else:
        print("invalid input")
def sub(num1, num2):
    if type(num1) is int or type(num1) is float and type(num2) is int or type(num2) is float:
        print(num1-num2)
    else:
        print("invalid input")
def mul(num1, num2):
    if type(num1) is int or type(num1) is float and type(num2) is int or type(num2) is float:
        print(num1*num2)
    else:
        print("invalid input")
def div(num1, num2):
    if type(num1) is not int and type(num1) is not float or type(num2) is not int and type(num2) is not float:
        print("invalid input")
    elif num2 == 0:
        print("u cant divide with zero")
    else:
        print(num1/num2)

def pow(num1, num2):
    if type(num1) is not int and type(num1) is not float or type(num2) is not int and type(num2) is not float:
        print("invalid input")
    elif num2 == 0 and num1 ==0:
        print("undefined")
    else:
        print(num1 ** num2)

