import pyttsx3
print(" WELCOME TO MY ROBO SPEAKER\n \n TO QUIT OUR PROGRAM ENTER 'quit'  \n")
while(True):
    text = pyttsx3.init()
    answer = str(input("What you want to text: "))
    if answer == "quit" :
        text.say("GOOD BYE THANKS FOR USING ROBO SPEAKER ")
        text.runAndWait()
        print("\n  THANKS FOR USING ROBO SPEAKER  ")
        break
    text.say(answer)
    text.runAndWait()