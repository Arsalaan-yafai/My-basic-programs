print("Welcome to Arsalaan Yafai calculator")
print("Enter your first number:")
var1 = int(input())
print("Enter your oppression:")
var2 = str(input())
print("Enter your second number:")
var3 = int(input())
if var2 == '+':
    print("Your result is:",var1+var3)
elif var2 == "-":
    print("Your result is:",var1-var3)
elif var2 == "*":
    print("Your result is:",var1*var3)
elif var2 == '/':
    print("Your result is:",var1/var3)
else:
    print("Your oppression is not valid")