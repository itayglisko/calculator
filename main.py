
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

if __name__ == '__main__':

    print("1.add\n2.substruction\n3.multipication\n4.division\n5.power")
    match input("enter 1 for add 2 for substruction etc\n"):
        case '1':
            add(5,7)
        case '2':
            sub(5,7)
        case '3':
            mul(-5,9)
        case '4':
            div(-5,7)
        case '5':
            pow(0,0)
        case _:
            print("invalid input!")
