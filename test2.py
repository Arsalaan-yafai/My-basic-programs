a=int(input("Enter a number: \n"))
if a>10 :
    print("Enter the right number ")
elif a<= 10:
    while (True):
        print(a)
        a=a+a
     



number = int(input ("Enter the number of which the user wants to print the multiplication table: "))
# We are using "for loop" to iterate the multiplication 10 times
print ("The Multiplication Table of: ", number)
for count in range(1, 11):
   print (number, 'x', count, '=', number * count)