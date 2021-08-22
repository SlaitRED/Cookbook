"""To do: improve this calculator!!!"""

num1 = float(input(" "))
opr = input("operation: ")
num2 = float(input(" "))

if (opr == "*"):
    print(num1, "*", num2, "=", num1 * num2)
elif (opr == "/"):
    print(num1, "/", num2, "=", num1 / num2)
elif (opr == "+"):
    print(num1, "+", num2, "=", num1 + num2)
elif (opr == "-"):
    print(num1, "-", num2, "=", num1 - num2)
else:
    print("Err001")
