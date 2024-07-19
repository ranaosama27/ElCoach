import pyttsx3

engine = pyttsx3.init()

engine.setProperty("rate", 100)
voices = engine.getProperty("voices")
print(voices)
def voice(text):
    engine.setProperty("voice", voices[1].id)
    engine.say(text)
    engine.runAndWait()
