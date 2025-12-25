import pyttsx3
import threading

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

def speak_async(text):
    thread = threading.Thread(
        target=lambda: (engine.say(text), engine.runAndWait())
    )
    thread.daemon = True
    thread.start()
