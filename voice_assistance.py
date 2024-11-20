import pyttsx3 #text to speech
import speech_recognition as sr #speech to text
import datetime
import wikipedia
import webbrowser
import os
import aifc

engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon...!")
    else:
        speak("Good Evening!...")

    speak("I am spandy Mam. Please tell me how can I help you")

def takecommand():
    #it takes microphone input from the user and returns string output

    r=sr.Recognizer()
    with sr.Microphone() as source: #listen commands we are giving to microphone
        print("Listening...")
        r.pause_threshold = 1 #the no. of second the system will take to recognize voice
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio , language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query


if _name_=="__main__":
    wishMe()
    while True:
        query = takecommand().lower()

        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results= wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir ="C:\\Musicfor_program"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strtime("%H:%M:%S")
            speak(f"Mam, the time is {strTime}")
            
        elif 'open code' in query:
            codepath = "C:\\Users\\ADMIN\\Desktop\\python\\voice_assistance.py"
            os.startfile(codepath)                    
