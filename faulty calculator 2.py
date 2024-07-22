print("Welcome to my calculator\n")
print("Enter your first number")
num1 = int(input())
print("Enter your oppression")
opp = str(input())
print("Enter your second number")
num2 = int(input())
if opp == "+" and num1 == 80 and num2 == 20 or num1 == 20 and num2 == 80:
    print("your result is",90)
elif opp == "+":
    print("Your result is",num1 + num2)
if opp == "-" and num1 == 80 and num2 == 20 or num1 == 20 and num2 == 80:
    print("your result is",70)
elif opp == "-":
    print("Your result is",num1 - num2)
if opp == "*" and num1 == 800 and num2 == 20 or num1 == 20 and num2 == 800:
    print("your result is",1700)
elif opp == "*":
    print("Your result is",num1 * num2)
if opp == "/" and num1 == 800 and num2 == 2 or num1 == 20 and num2 == 80:
    print("your result is",450)
elif opp == "/":
    print("Your result is",num1 / num2)
print("\nTHANKS FOR USING MY CALCULATOR. BEST OF LUCK FOR YOUR EXAM")