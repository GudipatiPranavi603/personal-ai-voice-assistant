import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import pywhatkit as kit
import sys
import pyautogui as pi
import time
import operator
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Good Morning!")
        print("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
        print("Good Afternoon!")
    else:
        speak("Good Evening!")
        print("Good Evening!")
def OpenChatGpt(query):
    try: 
        path = 'https://chat.openai.com/'
        webbrowser.open(path)
        pi.click(x=897, y=979,clicks=1,interval=0,button='left')
        speak('what you want to search')
        command = takeCommand().lower()
        speak('searching ')
        pi.typewrite(command)
        time.sleep(1)
        pi.press('enter')
    except:
        speak("no working")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening...")
        r.pause_threshold = 0.5 
        audio = r.listen(source)
    try:
        print("Recognizing...")
        speak("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print('Tell me again...')
        return 'none'
    return query
def save_file(query):
    try:
        speak("saving the file")
        pi.hotkey("ctrl", "s")
        speak("what should i keep file name")
        fileName = takeCommand().lower()
        pi.typewrite(fileName)
        time.sleep(2)
        pi.press('enter')
    except:
        print("not saving file")
def search_wikipedia(query):
    try:
        print("Searching Wikipedia...")
        results = wikipedia.summary(query, sentences=2)
        print("According to Wikipedia")
        print(results)
        # Assuming speak() is a function that speaks out the text
        speak(results)
    except wikipedia.exceptions.DisambiguationError as e:
        print("Ambiguous search query. Please be more specific.")
        speak("Ambiguous search query. Please be more specific.")
    except wikipedia.exceptions.PageError as e:
        print("No information found on Wikipedia for this query.")
        speak("No information found on Wikipedia for this query.")

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query or 'tell me about' in query or 'what is' in query or 'when' in query:
            search_wikipedia(query)
        elif "open whatsapp" in query:
            path = "https://web.whatsapp.com/"
            webbrowser.open(path)
        elif 'close whatsapp' in query:
            speak("closeing whatsapp")
            pi.hotkey('alt','f4')
        elif 'hello bro' in query:
            speak("hello Akhilesh how can i help you today")
        elif 'what can you do' in query:
            speak("i can do your basic needs like opening youtube, chorome, notpad searching engens etc..")
        elif 'open youtube' in query:
            speak('opening youtube ....')
            print('opening youtube ....')
            webbrowser.open('https://www.youtube.com')
            time.sleep(1)
            pi.hotkey('alt', 'space')
            time.sleep(1)
            pi.press('x')
        elif 'go to search bar' in query:
            print('searching on youtube')
            speak('searching on youtube')
            time.sleep(1)
            pi.moveTo(728, 178, 1)
            pi.click(x=728, y=179, clicks=1, button='left')
            time.sleep(3)
            speak("what to search")
            command = takeCommand()
            print(command)
            pi.typewrite(command)
            time.sleep(1)
            pi.press('enter')
        elif 'search on youtube' in query :
            query = query.replace("search on youtube", "")
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        elif 'open chrome' in query:
            webbrowser.open("https://www.google.com")
        elif "close the chrome" in query:
            print("closing chrome")
            speak("closing chrome")
            os.system("taskkill /im chrome.exe /f")
        elif "open notepad" in query:
            speak('opening notepad')
            print('opening notepad')
            path = "C:\\Windows\\notepad.exe"
            os.startfile(path)
        elif 'type a message' in query:
            query = query.replace("type a message", "")
            path = "C:\\Windows\\notepad.exe"
            os.startfile(path)
            time.sleep(1)
            pi.write(query,0.4)
        elif "close notepad" in query:
            speak('closing notepad')
            print('closing notepad')
            os.system("taskkill /f /im notepad.exe")
        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'close the vs code' in query:
            pi.hotkey('alt','f4')
        elif "open chat gpt" in query:
            OpenChatGpt(query)
        elif 'go to gpt search' in query:
            speak('we are in search bar')
            pi.click(x=897, y=979,clicks=1,interval=0,button='left')
            speak('what you want to search')
            command = takeCommand().lower()
            speak('searching ')
            pi.typewrite(command)
            time.sleep(1)
            pi.press('enter')
        elif 'copy the code' in query:
            img = pi.locateCenterOnScreen('scr.png')
            pi.click(img)
        elif 'paste the code' in query:
            speak('passting code')
            pi.hotkey('ctrl', 'v')
        elif 'close the tab' in query:
            pi.hotkey('alt', 'f4')
        elif 'open new window' in query:
            pi.hotkey('ctrl', 'n')
        elif 'open new tab' in query:
            pi.hotkey('ctrl', 't')
        elif 'close new tab' in query:
            pi.hotkey('ctrl', 'w')
        elif 'go to next tab' in query:
            pi.hotkey('ctrl' , 'tab')
        elif "show histry" in query:
            pi.hotkey('ctrl','h')
        elif "open dark tab" in query:
            pi.hotkey('ctrl','shift','n')
        elif "search" in query:
            search_query = query.split("search")[-1].strip()
            pi.hotkey('ctrl', 'l')  
            pi.typewrite(search_query, interval=0.1)  
            pi.press('enter')  
        elif 'volume' in query:
            for _ in range(15):
                pi.press("volumeup")
        elif 'volume down' in query:
            for _ in range(15):
                pi.press("volumedown")
        elif "brightness down" in query:
            for _ in range(10):
                pi.hotkey('f3')
        elif 'press enter' in query:
            pi.press('enter')
        elif 'scroll top' in query:
            pi.scroll(-150)
        elif "scroll down" in query:
            pi.scroll(150)
        elif "play on this video" in query:
            pi.click(clicks=1,button='left')
        elif "click on this link" in query:
            pi.click(clicks=1,button='left')
        elif "stop" in query:
            pi.press('k')  
        elif "mute" in query:
            pi.press('m')
        elif "full screen" in query:
            pi.press('f') 
        elif "skip" in query:
            pi.press('l')  
        elif "go back" in query:
            pi.press('j')  
        elif "next video" in query:
            pi.press('shift') 
        elif "previous video" in query:
            pi.hotkey('shift', 'p')  
        elif "shutdown the laptop" in query:
            os.system("shutdown /s /t 1")
        elif "save the file" in query:
            save_file(query)