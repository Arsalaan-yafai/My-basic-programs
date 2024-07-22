from typing import Dict, Any

import requests
import pyttsx3
import json
print("WELCOME IN MY WEATHER APP\n")
API_KEY = "4d3fcd1843ceb5f55a666db827cbacda"

try :

    user_input = str(input("Enter the city: "))
    text = pyttsx3.init()
    weather_data =  requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={API_KEY}")
    #print(weather_data.json())
    if weather_data.json()['cod'] == '404':
        print("The city doesnot exist ")
        text.say("PLEASE ENTER RIGHT CITY")
        text.runAndWait()
    else:

        weather= weather_data.json()['weather'][0]['main']
        temp = int(weather_data.json()['main']['temp'])
        celcius_temp= int((temp-32)*5/9)
        minimum_temp = int(weather_data.json()['main']['temp_min'])
        minimum_celcius= int((minimum_temp-32)*5/9)
        maximum_temp = int(weather_data.json()['main']['temp_max'])
        maximum_celcius = int((maximum_temp-32)*5/9)
        humidity= weather_data.json()['main']['humidity']
        wind= weather_data.json()['wind']['speed']
        cloud= weather_data.json()['clouds']['all']
        """
        answer =["The temperature is: ",celcius_temp ,"\nThe weather is: ",weather,"\nThe minimum temperature is: ",minimum_celcius,"\nThe maxmium temperature is: ",maximum_celcius,"\nThe humidity is: ",humidity,"\nThe wind is: ",wind,"\nThe clouds is: ",cloud]
        print(answer)
        text.say(answer)
        text.runAndWait()
    """

        print("The Weather is: ",weather)
        print("The Temperature is: ",celcius_temp)
        print("The Minimum Temperature is: ",minimum_celcius)
        print("The Maximum Temperature is: ",maximum_celcius)
        print("The Humidity is: ",humidity)
        print("The percantage of  Clouds coverage is: ",cloud)
        print("The speed of Wind is: ",wind,"kmph")
        """
        text.say("The weather is ")
        text.say(weather)
        text.say("The temperature is")
        text.say(celcius_temp and "Degree celsius")
        #text.say("Degree celsius")
    
        text.runAndWait()
        """
        d1 = {"The weather is": weather}
        d2 = {"The temperature in degree celsius is" : celcius_temp }
        d3 = {"The humidity % is" : humidity}
        d4 = {"The maximum temperature in degree celsius is ": maximum_celcius}
        d5 = {"The minimum temperature in degree celsius is" : minimum_celcius}
        d6 = {"The speed of wind in kilomerter per hour is": wind}
        d7 = {"The percentage of cloud coverage is" : cloud}
        text.say(d1)
        text.say(d2)
        text.say(d5)
        text.say(d4)
        text.say(d3)
        text.say(d7)
        text.say(d6)
        text.runAndWait()
except:
    print("PLEASE CONNECT THE INTERNET CONNECTION")
    text.say("PLEASE CONNECT THE INTERNET CONNECTION TO ACCESS THE WEATHER")
    text.runAndWait()
