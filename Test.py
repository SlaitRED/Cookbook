
def getNo():
	result = float(input("Number: "))
	return result

def add():
	result = getNo() + getNo()
	return result

def Main():
	output = add()
	print(output)

if __name__=="__main__":
	Main()
