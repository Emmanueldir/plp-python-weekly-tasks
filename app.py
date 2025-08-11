x = input("Enter 1st number:")
y = input("Enter 2nd number:")
operand = input("Enter your operation e.g +, -: ")

match operand:
    case "+":
        result = int(x) + int(y)
        print(result)
    case "-":
        result = int(x) - int(y)
        print(result)
    case "*":
        result = int(x) - int(y)
        print(result)
    case "/":
        result = int(x) / int(y)
        print(result)