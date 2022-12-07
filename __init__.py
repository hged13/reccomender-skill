from mycroft import MycroftSkill, intent_file_handler


class Reccomender(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('reccomender.intent')
    def handle_reccomender(self, message):
        self.speak_dialog('reccomender')


def create_skill():
    return Reccomender()

