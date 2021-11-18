import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime

import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def talk(text):
    engine.say(text)
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "commander" in command:
                command = command.replace("commander", " ")
                print(command)
    except:
        talk("hi am wight commander give me a command then i answer you we can make conversatiton")
        print("hi am wight commander give me a command then i answer you we can make conversatiton")
        pass
    return command


def run_commander():
            command = take_command()
            print(command)
            if 'play' in command: 
                song = command.replace("play", " ")
                talk("playing" + song)
                pywhatkit.playonyt(song)
            elif 'time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                talk( "the time is" + time)
                print(time)
            elif 'search' in command:
                search = command.replace('search', "")
                Ans = wikipedia.summary(search,1)
                talk(Ans)
                print(Ans)
            else:
                talk("i can not understand your words buddy , can say again clearly")
                print("i can not understand your words buddy , can say again clearly")

run_commander()
