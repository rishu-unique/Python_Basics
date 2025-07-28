# Before running this code, ensure you have the 'pyttsx3' library installed.
# This code uses the pyttsx3 library to convert text to speech.

import pyttsx3

engine = pyttsx3.init()
engine.say("Hey I am good")

engine.runAndWait()