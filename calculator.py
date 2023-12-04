def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    return x / y
def rem(x, y):
    return x % y

print()
print("\u0332".join("Welcome to simple calculator! Let's calculate!"))
print()
# \u0332 is used to underline the contents that precedes it

# taking user input for operation and operands
print("""SELECT THE OPERATION:\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Divide-Remainder""")
num1=int(input("Please enter the first number:"))
num2=int(input("Please enter the second number:"))

choice = int(input("Enter choice - 1,2,3,4,5: "))
if choice == 1:
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == 2:
    print(num1, "-", num2, "=", sub(num1, num2))
elif choice == 3:
    print(num1, "*", num2, "=", mul(num1, num2))
elif choice == 4:
    print(num1, "/", num2, "=", div(num1, num2))
elif choice == 5:
    print(num1, "%", num2, "=", rem(num1, num2))
else:
    print("INVALID CHOICE!!")
