import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import sys
import pyautogui
import time
import json
import requests
import PyPDF2


def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    print(voices)
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 290)
    engine.say(text)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 5, 10)
    try:
        print('Recognising.....')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said; {query}")
    except Exception as e:
        return ""
    return query.lower()


def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <= 12:
        speak("Good morning sir")

        print("good morning sir")

    elif hour > 12 and hour <= 18:
        speak("Good afternoon sir")

        print("good afternoon sir")

    else:
        speak("Good evening sir")

        print("good evening sir")

    speak("IAM JARVIS. HOW CAN I HELP YOU")


def pdf_reader():
    book = open('1.pdf', 'rb')
    pdf_reader = PyPDF2.PdfReader(book)
    pages = len(pdf_reader.pages)
    speak(f"total number of pages in this book is {pages}")
    speak("sir please enter the page number which i should read")
    pg = int(input("Please enter the page number: "))
    page = pdf_reader.pages[pg]
    text = page.extract_text()
    speak(text)


wish()
text = take_command
speak(text)
# take_command()
while True:
    # if 1:
    query = take_command().lower()
    if "open notepad" in query:
        npath = "C:\\Windows\\notepad.exe"
        os.startfile(npath)
    elif "open terminal" in query:
        os.system("start cmd")
        """
    elif "open camera" in query:
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Error: Could not open camera.")
        else:
            cv2.namedWindow("webcam")
            while True:
                ret, image = cap.read()
                if not ret:
                    print("Error: Failed to capture image from camera.")
                    break
                cv2.imshow('webcam', image)
                k = cv2.waitKey(50)
                if k == 27:  # Press 'Esc' to exit
                    break
            
            cap.release()
            cv2.destroyAllWindows()
            sys.exit()
        """
    elif "play music" in query:
        music_dr = "C:\\nasheed"
        songs = os.listdir(music_dr)
        rd = random.choice(songs)
        os.startfile(os.path.join(music_dr, rd))
    elif "ip address" in query:
        ip = get('https://api.ipify.org').text
        speak(f"Your ip address is {ip}")
        print(ip)
    elif "wikipedia" in query:
        try:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=3)
            speak("according to wikipedia")
            speak(result)
            print(result)
        except:
            speak("result not found")
    elif "open youtube" in query:
        webbrowser.open("www.youtube.com")
    elif "open whatsapp" in query:
        webbrowser.open("web.whatsapp.com")
    elif "open amazon" in query:
        webbrowser.open("amazon.in")
    elif "open google" in query:
       # webbrowser.open("google.com")
        speak("sir what should i search on google")
        ay = take_command().lower()
        webbrowser.open(f"{ay}")
    elif "send message to you" in query:
        kit.sendwhatmsg("+917097083409", "testing", 1, 2)
    elif "play faded in youtube" in query:
        kit.playonyt("alan walker faded")
    elif "play python in youtube" in query:
        kit.playonyt("python in one video by code with harry")
    elif "play mohammed ali in youtube" in query:
        kit.playonyt("muhammed ali youth club")
    elif "play hasi tv in youtube" in query:
        kit.playonyt("hasi tv")
    elif "change window" in query:
        pyautogui.keyDown("alt")
        pyautogui.press("tab")
        time.sleep(1)
        pyautogui.keyUp("alt")

    elif "where we are" in query:
        speak("let me check, please wait for some moment sir")
        try:
            ipAdd = requests.get('https://api.ipify.org').text
            print(ipAdd)
            url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
            geo_request = requests.get(url)
            geo_data = geo_request.json()
            city = geo_data['city']
            #state = geo_data['state']
            country = geo_data['country']
            speak(
                f"sir iam not sure, but i think we are in {city} city of {country}")
        except Exception as e:
            speak("sorry sir due to network issue i cant find where we are")
            pass

    elif "take screenshot" in query:
        speak("sir please tell me the file name for screenshot file")
        name = take_command().lower()
        speak("sir please hold the screen for few seconds. iam taking the screenshot")
        time.sleep(3)
        img = pyautogui.screenshot()
        img.save(f"{name}.png")
        speak("iam done sir, the screenshot is saved")

    elif "read pdf" in query:
        pdf_reader()

    elif "no thanks" in query:
        speak("thanks for using me sir, have a good day.")
        sys.exit()

    speak("sir do you have any other work...")
