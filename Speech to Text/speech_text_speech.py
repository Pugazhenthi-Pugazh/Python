import speech_recognition as sr
import pyaudio

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speech anything: ")
    audio=r.record(source,  duration=5)
    print("please wait..")
   
    try:
       print("You said: "+ r.recognize_google(audio))
       
    except:
        print("Sorry could not recognize your voice")
    
    
