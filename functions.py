#First function
def print_function():
    print("Hello")
    print("Goodbye")

print_function()

# Can be used to recall pre-defined code, which can be used multiple times

def greet_by_name(name="user", greeting="Hello"):
    #Function with variables
    print(greeting + ", " + name)

greet_by_name()
greet_by_name(input("What is your name? "))
greet_by_name("Rafael", "Welcome")
greet_by_name(greeting="Greetings", name="Rafael")

def cube(base_number):
    cubed_value = base_number * base_number * base_number
    return cubed_value

print (cube(11))
twelve_cubed = cube(12)
print(twelve_cubed)