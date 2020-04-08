from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_file_handler, intent_handler


class CoronavirusInfoSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('info.coronavirus.intent')
    def handle_info_coronavirus(self, message):
        self.speak_dialog('info.coronavirus')
    
    def initialize(self):
        # TO-DO! 
        pass
    
    def stop(self):
        self.stop_beeping()

def create_skill():
    return CoronavirusInfo()

