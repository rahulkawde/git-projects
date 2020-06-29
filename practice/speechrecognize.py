import pyttsx3
from datetime import datetime 
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')       #getting details of current voice
# engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[38].id)
# engine.say("I will speak this text")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def take_command():
    r= sr.Recognizer()
    with sr.Microphone()as source:
        print('listening.....')
        r.pause_threshold=1
        audio= r.listen(source)
    try:
        print('recognizing...')
        quary= r.recognize_google(audio,language='en-in')
        print(f'user said : {quary}\n')
    except Exception as e:
        print('say that again please')
        return (None)
    return quary
    

if __name__ == "__main__":
    speak('hello sir')

    def wish_me():
        hour = datetime.now().hour
        hour = int(hour)
        if hour >= 0 and hour < 12:
            speak('good morning sir')
        elif hour >= 12 and hour < 18:
            speak('good afternoon sir') 
        else:
            speak('good evening sir') 
        speak('this is friday , how can i help you sir')       

wish_me()
# print(datetime.now())
take_command()


