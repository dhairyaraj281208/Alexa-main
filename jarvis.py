import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from playsound import playsound
import time
from code import code
from wish import *

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[2])
engine.setProperty('voice', voices[1].id)


def speak(audio):
        print("Alexa: ", audio)
        engine.say(audio)
        engine.runAndWait()


def speakWithoutSubs(audio):

        engine.say(audio)
        engine.runAndWait()




def takeCommand():
    try:
        query = str(input("You: "))
        return query
    except Exception as e:
                speak("Sorry sir, I am not able to recognize! Please repeat!")


def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('maloobrothers28@gmail.com', 'maloo1008')
        server.sendmail('maloobrothers28@gmail.com', to, content)
        server.close()
    except Exception as e:
                speak("Sorry sir, i am not able to do this task!")


def news():
    try:
        speak("English or Hindi")
        f = str(input("You: "))
        if 'english' in f:
            webbrowser.open(
                "https://epaper.hindustantimes.com/rajasthan?eddate=27/04/2021&Pageview=list")
        elif 'hindi' in f:
            webbrowser.open("https://epaper.bhaskar.com/state/rajasthan")
        else:
            speak("Sorry sir i am not able to show you news!")
    except Exception as e:
                speak("Sorry sir, i am not able to do this task!")


def countdown(time_sec):
    try:
        while time_sec:
            min = time_sec
            timeformat = '{:02d}:{:02d}'.format(0, time_sec)
            print(timeformat, end='\n',)
            speakWithoutSubs(time_sec)
            time.sleep(1)
            time_sec -= 1
    except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

    speak("Sir the time is up!")


def random(max, min):
    try:
        import random
        speak(random.randint(min, max))
    except Exception as e:
                speak("Sorry sir, i am not able to do this task!")


def codegiving(password):
    try:
        if password == 'maloo1133':
            print(code)
            speak("This is my code")
    except Exception as e:
                speak("Sorry sir, i am not able to do this task!")




if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        
        friends = ["Goral", "Devendra", "Lakshaya", "Manan", "Manjeet", "Manvendra", "Naman", "Pushkar", "Ronak", "Kabir", "Kushal", "Udit", "Tarun", "Aarav", "Karan"]
        if 'wikipedia' in query:
            try:
                speak('Searching Wikipedia...')
                speak("What should i search")
                b = str(input("You: "))
                query = query.replace("wikipedia", b)
                results = wikipedia.summary(query, sentences=3)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'open youtube' in query:
            try:
                webbrowser.open("youtube.com")
                speak("opening youtube")  
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")
        

        elif 'open google' in query:
            try:
                webbrowser.open("google.com")
                speak("opening google")
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'open stackoverflow' in query:
            try:
                webbrowser.open("stackoverflow.com")
                speak("opening open stackoverflow")
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'open whitehat jr' in query:
            try:
                webbrowser.open("https://code.whitehatjr.com/s/dashboard")
                speak("Opening whitehat jr")
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'who are you' in query:
            try:
                speak("I am your Virtual Assistant Alexa sir! How can I help you.")
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'play music' in query:
            try:
                playsound('play.wav')
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'open playlist' in query:
            try:
                codePath1 = "C:\\Users\\Dhairya\\Desktop\\music library"
                os.startfile(codePath1)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'the time' in query:
            try:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                print(f" {strTime}")
                speak(f"Sir, the time is {strTime}")
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'the date' in query:
            try:    
                strdate = datetime.datetime.now().strftime("%D")
                print(f" {strdate}")
                speak(f"Sir, the date is {strdate}")
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'the year' in query:
            try:
                strYear = datetime.datetime.now().strftime("%Y")
                print(f" {strYear}")
                speak(f"Sir, the year is {strYear}")
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'open code' in query:
            try:
                codePath = "C:/Users/Dhairya/AppData/Local/Programs/Microsoft VS Code/Code"
                os.startfile(codePath)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'send a email' in query:
            try:
                speak("Whom should I send?")
                to = takeCommand()
                speak("What should I say?")
                content = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")

        elif 'give me you code' in query:
            try:
                speak("Please give me the password")
                e = str(input("You: "))
                codegiving(e)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'news' in query:
            try:
                news()
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")
        elif 'updates' in query:
            try:
                news()
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'who is your author' in query:
            try:
                speak("My Author is the great coder dhairya raj malu")
                print('''
                Author = Dhairya raj maloo
                ''')
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'my coding' in query:
            try:
                codePathi = "C:/Users/Dhairya/Desktop/Coding"
                os.startfile(codePathi)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'what you can do' in query:
            try:
                speak('''
                I am alexa sir
                i can do many things
                Like telling time date year 
                searching anything you want in wikipedia
                showing news
                giving my code
                sending emails to any id
                and more features
                ''')
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'what are your features' in query:
            try:
                speak('''
                I am alexa sir
                I can do many things
                Like telling time date year 
                searching anything you want in wikipedia
                showing news
                giving my code
                sending emails to any id
                and more features
                ''')
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'set timer' in query:
            try:
                speak("For how many seconds")
                h = int(input("You: "))
                countdown(h)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'random number' in query:
            try:
                speak("What should be the maximum number?")
                m = int(input("You: "))
                speak("What should be the minimum number?")
                n = int(input("You: "))
                random(m, n)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'friends' in query:
            try:
                speak(friends)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'add friend' in query:
            try:
                speak("Whom should I add ?")
                g = str(input("You: "))
                h = friends.append(g)
                speak("Added Successfully")
                print(friends)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'remove friend' in query:
            try:
                speak("Whom should I remove?")
                j = str(input("You: ")) 
                friends.remove(j)
                speak("Removed Successfully !")
                print(friends)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'add' in query:
            try:
                speak("What is the first number ?")
                a = int(input("You: "))
                speak("What should be the second number ?")
                b = int(input("You: "))
                speak(a + b)
                a= str(a)
                b = str(b)
                speak("Is the Sum of " + a + " and " + b)
            except Exception as e:
                speak("Mere dimag chal namhi raha hai. Apne App Dhond lo!")
        
        elif 'sum' in query:
            try:
                speak("What is the first number ?")
                a = int(input("You: "))
                speak("What should be the second number ?")
                b = int(input("You: "))
                speak(a + b)
                a= str(a)
                b = str(b)
                speak("Is the Sum of " + a + " and " + b)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        
        elif 'difference' in query:
            try:
                speak("What is the first number ?")
                a = int(input("You: "))
                speak("What should be the second number ?")
                b = int(input("You: "))
                speak(a - b)
                a= str(a)
                b = str(b)
                speak("Is the difference of " + a + " and " + b)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'subtract' in query:
            try:
                speak("What is the first number ?")
                a = int(input("You: "))
                speak("What should be the second number ?")
                b = int(input("You: "))
                speak(a - b)
                a= str(a)
                b = str(b)
                speak("Is the difference of " + a + " and " + b)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'multiply' in query:
            try:
                speak("What is the first number ?")
                a = int(input("You: "))
                speak("What should be the second number ?")
                b = int(input("You: "))
                speak(a * b)
                a= str(a)
                b = str(b)
                speak("Is the product of " + a + " and " + b)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'divide' in query:
            try:
                speak("What is the divident ?")
                a = int(input("You: "))
                speak("What should be the divisor ?")
                b = int(input("You: "))
                speak(b / a)
                a= str(a)
                b = str(b)
                speak("Is the product of " + a + " and " + b)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")


        elif 'change name of a file' in query:
            try:
                speak("Which file on Deskop ?")
                k = str(input("You: "))
                speak("What's the new name")
                d = str(input("You: "))
                f = "C:\\Users\\hp\\Desktop\\" + d 
                g = "C:\\Users\\hp\\Desktop\\" + k
                os.renames(g , f)
                speak("Successfully renamed!")
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'who is ' in query:
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speakWithoutSubs(results)
            except Exception as e:
                speak("Sorry sir, i am not able to do this task!")

        elif 'quit' in query:
            speak("Thank you sir!")
            os.system(quit())

        elif 'sabji' in query:
            sabji()

                      
        else:
            speak("Sorry sir I am not able to get it! Please repeat what you said")