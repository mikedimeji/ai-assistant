# src/core/voice_manager.py
import pyttsx3

class VoiceManager:
    def __init__(self):
        self.engine = pyttsx3.init()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()