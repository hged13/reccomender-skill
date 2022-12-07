from mycroft import MycroftSkill, intent_file_handler
import pandas
import csv


class Reccomender(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('reccomender.intent')
    def handle_reccomender(self, message):
        self.speak_dialog('reccomender')
    
    
    def get_user(self):
        file = open('/home/pi/.config/mycroft/skills/NewUserCreation/log.csv', 'r')
        df = pd.read_csv(file)


def create_skill():
    return Reccomender()

