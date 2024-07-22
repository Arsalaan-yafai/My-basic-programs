def function1():
    num1 = 50
    print("Enter Your Number: \n")
    num2 = int(input())
    while (True):
        if num2 > num1:
            print("Your number is greater \n")
            print("Enter your number: ")
            num2 = int(input())
            continue

        elif num2 < num1:
            print("Your number is lesser \n")
            print("Enter your number: ")
            num2 = int(input())
            continue
        elif num2 == num1:
            print("Congratulations You Won ")
            break


function1()

