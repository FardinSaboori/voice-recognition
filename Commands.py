import os
import pyttsx3
engine = pyttsx3.init()


class Commander:
    def __init__(self):
        self.confirm = ["yes", "affirmative", "Yeah", "do it"]
        self.cancel = ["no", "negative", "cancel"]

    def discover(self, text):
        if "what" in text and "your name" in text:
            if "my" in text:
                self.respond("you haven't told me your name")
            else:
                self.respond("my name is Fardin Commander, How are you?")
        else:
            self.respond("Hello")

    def respond(self, response):
        engine.say(response)
        engine.runAndWait()
