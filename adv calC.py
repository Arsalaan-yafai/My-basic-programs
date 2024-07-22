while(True):
    var4 = input("PRESS Y TO CONTINUE:\n PRESS X TO BREAK:")
    if var4=="Y":
        continue
    elif var4=="X":
       break

var1= int(input("Enter Your Number: "))
var2= input("Enter the oppression: ")
var3= int(input("Enter your second number: "))
if var2== "+":
    print("Your result is: ",var1+var3)
elif var2=="-":
    print("Your result is: ",var1-var3)
elif var2=="*":
    print("Your result is: ",var1*var3)
elif var2=="/":
    print("Your result is: ",var1/var3)
else:
    print("Enter Right Oppression")
while(True):
    var4 = input("PRESS Y TO CONTINUE:\n PRESS X TO BREAK:")
    if var4=="Y":
        continue
    elif var4=="X":
     break



