import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia as wiki


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():

    speak("Welcome")
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    print(Time)
    speak(f"The current time is {Time}")

time()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing")
        speak("Searching Wikipedia")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
        result = wiki.summary(query, sentences=4)
        speak("According to Wikipedia")
        print(result)
        speak(result)

    except Exception as e:
        print(e)
        print("Say that again")
        speak("Say that again")
        return None
    return query

takecommand()

