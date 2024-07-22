print("Enter your first number: ")
var1=int(input())
print("Enter your oppression: ")
var2=input()
print("Enter your 2nd number: ")
var3= int(input())
if var1== 20 and var2== "+" and var3 == 50:
    print("Your result is:", var1+var3-10)
elif var2== "+":
    print("Your result is:  ",var1+var3)

elif var1==45 and var2== "*" and var3== 2:
    print("Your answer is: ",var1*var3+10)
elif var2=="-":
    print("Your result is: ",var1-var3)
elif var2=="*":
    print("Your result is: ",var1*var3)
elif var2=="/":
    print("Your result is: ",var1/var3)
elif var2 != "+" and "-"and "*"and "/":
    print ("Enter right oppression: ")

