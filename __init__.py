from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_file_handler, intent_handler


class CoronavirusInfoSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.learning = True
        
    @intent_file_handler('situation.coronavirus.intent')
    def handle_info_coronavirus(self, message):
        self.speak_dialog('situation.coronavirus')
    
    @intent_file_handler('symptoms.coronavirus.intent')
    def handle_info_coronavirus(self, message):
        self.speak_dialog('symptoms.coronavirus')
    
    @intent_file_handler('information.coronavirus.intent')
    def handle_info_coronavirus(self, message):
        self.speak_dialog('information.coronavirus')

    @intent_file_handler('shopping.info.corona.intent')
    def handle_info_coronavirus(self, message):
        self.speak_dialog('shopping.info.corona')
     
    @intent_file_handler('news.coronavirus.intent')
    def handle_info_coronavirus(self, message):
        self.speak_dialog('news.coronavirus.dialog')

def create_skill():
    return CoronavirusInfoSkill()
