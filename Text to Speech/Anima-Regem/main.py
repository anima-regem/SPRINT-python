import pyttsx3

def speak():

    engine = pyttsx3.init()

    text = input("Enter text : ")

    engine.say(text)
    engine.runAndWait()

speak()