import speech_recognition as sr
import webbrowser
import pyttsx3
import time
import musicliberary
from google import genai
import os


def speak(text):
    print("Speaking:", text)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    print("Done speaking")

def aiProcess(command):
    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=command,
        config={
            "system_instruction": (
                "You are a voice assistant named Jarvis. "
                "Answer in 1-2 short spoken sentences, under 30 words. "
                "No markdown, no bullet points, no headers — plain conversational speech only."
            )
        }
    )

    return response.text


def processCommand(c):
    c = c.lower().strip()
    if "open google" in c:
        webbrowser.open("http://google.com")
    elif "open facebook" in c:
        webbrowser.open("http://facebook.com")
    elif "open youtube" in c:
        webbrowser.open("http://youtube.com")
    elif "open linkedin" in c:
        webbrowser.open("http://linkedin.com")
    elif c.startswith("play"):
        song=c.lower().split(" ")[1]
        link = musicliberary.music[song]
        webbrowser.open(link)
    else:
       output = aiProcess(c)
       speak(output)

if __name__=="__main__":

    speak("Initializing Jarvis")

    while True:
        # Listen for the wake word Jarvis
        # Obtain audio from the microphone
        r=sr.Recognizer()
        
        print("Recognizing")
        # Recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Listening....")
                r.adjust_for_ambient_noise(source, duration=0.5)
                audio = r.listen(source, timeout=2, phrase_time_limit=2)

            word = r.recognize_google(audio)
            print("Heard:", repr(word))

            if "hello jarvis" in word.lower().strip():
                print("Wake word detected")
                speak("how may i help you?")

                with sr.Microphone() as source:
                    print("Jarvis Active....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)

        except sr.WaitTimeoutError:
            print("No speech detected in time window")
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech API; {}".format(e))
        except Exception as e:
            print("Jarvis error: {}".format(e))