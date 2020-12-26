import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import subprocess



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def aboutme():

    speak("Hello mam. i am assistaa, your virtual assistant. How Can I help you?")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    aboutme()
    while True:

        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia of ' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            open_google = webbrowser.get(
                'windows-default').open('https://youtube.com')

        elif 'open google' in query:
            open_google = webbrowser.get(
                'windows-default').open('https://google.com')

        elif 'open facebook' in query:
            open_google = webbrowser.get(
                'windows-default').open('https://facebook.com')

        elif 'open instagram' in query:
            open_google = webbrowser.get(
                'windows-default').open('https://instagram.com')

        elif 'play music' in query:
            music_dir = 'D:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"mam, the time is {strTime}")

        elif 'open code blocks' in query:
            speak("opening codeblocks")
            codePath = "C:\\Program Files\\CodeBlocks\\codeblocks"
            os.startfile(codePath)

        elif 'open paint' in query:
            speak("opening paint")
            subprocess.Popen('C:\\Windows\\system32\\mspaint.exe')

        elif 'open notepad' in query:
            speak("opening notepad")
            subprocess.Popen('C:\\Windows\\system32\\notepad.exe')

        elif 'open powerpoint presentation' in query:
            speak("opening Power Point presentation")
            power = r'C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.exe'
            os.startfile(power)

        elif 'open ms word' in query:
            os.startfile(
                'C:\\Program Files\\Microsoft Office\\root\\Office16\\winword.exe')

        elif 'tell a joke' in query:
            speak(pyjokes.get_joke())

        elif 'open my movies' in query:
            os.startfile('E:\\New movies')

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you,mam")

        elif 'search' in query:
            query = query.replace("search", "")
            webbrowser.open_new_tab(query)
            

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()
