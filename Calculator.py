#TODO improve this calculator!!!

num1 = float(input("Number 1: "))
opr = input("Function: ")
num2 = float(input("Number 2: "))

if(opr == "*"):
    print("Result: ", num1 * num2)
elif(opr == "/"):
    print("Result: ", num1 / num2)
elif (opr == "+"):
    print("Result: ", num1 + num2)
elif(opr == "-"):
    print("Result: ", num1 - num2)
else:
    print("Bad function :(")