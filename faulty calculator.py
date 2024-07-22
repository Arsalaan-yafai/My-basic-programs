print("Welcome to my calculator\n")
print("Enter your first number")
num1=int(input())
print("Enter your oppression")
opp=str(input())
print("Enter your second number")
num2=int(input())
if opp == "+" and num1 == 50 and num2==20 or num1== 20 and num2 == 50:
    print(80)
elif opp == "+":
    print("Your answer is",num1+num2)
if opp == "-" and num1==50 and num2==20 or num1== 20 and num2 == 50:
    print(80)
elif opp == "-":
    print("Your answer is", num1 - num2)
if opp == "*" and num1==50 and num2==20 or num1== 20 and num2 == 50:
    print(80)
elif opp == "*":
    print("Your answer is", num1 * num2)
if opp == "/" and num1 == 50 and num2 == 20 or num1 == 20 and num2 == 50:
        print(80)
elif opp == "/":
    print("Your answer is", num1 / num2)
print("\nThanks for using my calculator\n")
print("CREATED BY ARSALAAN YAFAI")