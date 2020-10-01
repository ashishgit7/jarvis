import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good morning !")
    elif hour>=12 and hour<18:
        speak("Good afternoon!")
    else:
        speak("good evening")
    speak("Hello Mister Ashish Gupta , How may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("yes sir...")
        r.pause_threshold = 1.2
        audio = r.listen(source,phrase_time_limit=5)
    try:
        print("Recognizing..")
        query = r.recognize_google(audio,language = "en-in")
        print("user said:",query)
    except Exception as e:
        speak("sorry sir can't help because of given error")
        #print(e)
        speak("say that again please")
        return "None"
    return query
if __name__ == "__main__":
    wishMe()
    #while True:
    query = takeCommand().lower()
    
    if 'wikipedia' in query:
        speak('searching wikipedia..')
        query = query.replace("wikipedia","")
        result = wikipedia.summary(query,sentences=2)
        speak("according to wikipedia")
        print(result)
        speak(result)
        
    elif 'youtube' in query:
        webbrowser.open('youtube.com')
        
    elif 'google' in query:
        webbrowser.open('google.com')
        
    elif 'the time' in query:
        strtime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strtime}")

