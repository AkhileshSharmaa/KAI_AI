import speech_recognition as sr
import pyttsx3

from commands import processCommand
from responses import get_random_response

def speak(text):
    engine = pyttsx3.init("sapi5")
    print("KAI:", text)
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":

    speak("Initializing KAI.")
    first_time = True

    while True:

        r = sr.Recognizer()

        try:
            with sr.Microphone() as source:

                print("\nListening...")

                r.adjust_for_ambient_noise(source, duration=0.5)
                audio = r.listen(source, timeout=5, phrase_time_limit=2)

            print("Recognizing...")

            word = r.recognize_google(audio)

            print("You said:", word)

            if word.lower() == "kai":

                if first_time:
                    speak("Hey! What can I do for you?")
                    first_time = False

                else:
                    speak(get_random_response())

                with sr.Microphone() as source:

                    print("KAI Active... waiting for a command...")

                    r.adjust_for_ambient_noise(source, duration=0.5)

                    audio = r.listen(source, timeout=5, phrase_time_limit=8)

                command = r.recognize_google(audio)
                
                print("Command:", command)

                if command.lower() in ["goodbye", "exit", "quit", "shutdown"]:
                    speak("Goodbye.")
                    break

                speak("Got it.")

                processCommand(command, speak)
        
        except sr.WaitTimeoutError:
            print("No speech detected.")

        except sr.UnknownValueError:
            print("Could not understand the audio.")

        except sr.RequestError as e:

            print("Could not request results from "
                  "Google Speech Recognition service:",e)

        except KeyboardInterrupt:
            
            print("\nExiting KAI...")
            speak("Goodbye.")
            break