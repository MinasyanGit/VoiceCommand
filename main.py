import speech_recognition as sr
import os
import sys
import webbrowser


def talk(words):
    print(words)
    os.system("say " + words)


def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=0.1)
        audio = r.listen(source)

    try:
        task = r.recognize_google(audio).lower()
        print("You say " + task)
    except sr.UnknownValueError:
        talk("I don't understand ")
    return task


def make_something(task):
    if 'clear' in task:
        talk("opening")
        url = "https://www.google.com/?client=safari"
        webbrowser.open(url)
        webbrowser.open(url)
    elif 'stop' in task:
        talk("Of course")
        sys.exit()


while True:
    make_something(command())
