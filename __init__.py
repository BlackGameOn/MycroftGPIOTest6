from mycroft import MycroftSkill, intent_handler
import sys
import requests
import json
import threading

from adapt.intent import IntentBuilder

__author__ = 'BlackGame'

class LedControl(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.load_data_files(dirname(__file__))

        command_intent = IntentBuilder("IoCommandIntent").require("komut").require("komutarg").build()

        self.register_intent(command_intent, self.handle_led_intent)        

    def handle_led_intent(self, message):
        if message.data["komut"].upper() == "Turn LED":
            if message.data["komutarg"].upper() == "On":
                python //home//pi//kerems//LED_AC.py
                self.speak_dialog("ledacildi")
            if message.data["komutarg"].upper() == "Off":
                python //home//pi//kerems//LED_KAPAT.py
                self.speak_dialog("ledkapatildi")

def create_skill():
    return LedControl()

