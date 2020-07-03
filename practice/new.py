import speech_recognition as sr
# called recognizer
r = sr.Recognizer()
# open audio file or use microphone
with sr.Microphone() as source:
    print('speak anything :')   
    audio = r.listen(source)        # store in audio
    try:
        text = r.recognize_google(audio)    # convert audio to text
        print('you said: {}'.format(text))  # show the text
    except:
        print('cann\'t recognize your audio...')    
