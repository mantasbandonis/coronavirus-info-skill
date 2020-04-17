from mycroft import MycroftSkill, intent_file_handler, intent_handler
from mycroft.util import play_mp3
from mycroft.audio import wait_while_speaking
from time import time, sleep

class CoronavirusInfoSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.learning = True

    def initialize(self):
        self.url_value = self.translate_namedvalues('url.value')

        
    @intent_file_handler('situation.coronavirus.intent')
    def handle_situation_coronavirus(self, message):
        #self.speak_dialog('situation.coronavirus')
        answer_situation = self.get_response('situation.coronavirus')
        exit = self.handle_info(answer_situation)
        if exit is True:
            return
        else:
            answer_anders = self.get_response("Möchtest du vielleicht noch etwas anderwes wissen?")
            self.handle_info(answer_anders)

    def handle_info(self, answer_situation):
        self.log.info(answer_situation)
        if self.voc_match(answer_situation, "news"):
            sleep(3)
            self.speak("Okay, ich spiele die neuen Nachrichten von Ö3 zu dem Coronavirus")
            sleep(4)
            wait_while_speaking()
            play_mp3(self.url_value["url"])
            exit = True
            return exit
        
        elif self.voc_match(answer_situation, "symptoms"):
            self.speak_dialog('symptoms.info.corona')

            confirm_save = self.ask_yesno("Verspühren sie selber Symptome?")
            if confirm_save == "yes":
                 self.speak("Bitte kontaktieren sie umgehen die Gesundheitstelefonnummer 1450 und lassen sie sich beraten")
            elif confirm_save == "no":
                self.speak("Sehr gut! Bleiben sie gesund", expected_response=False)
 
        elif self.voc_match(answer_situation, "sale"):
            answer_einkaufen = self.ask_yesno("Möchtest du etwas zur empfohlenen Einkaufszeit wissen?")
            if answer_einkaufen == "yes":
                self.speak("Okay, folgendes:")
                self.speak_dialog('shopping.info.corona')
                    
            elif answer_anders == "no":
                elf.speak("Okay, danke ich bin gerne für dich da", expect_response=False)

            else:
                self.speak("Okay, danke ich bin gerne für dich da", expect_response=False)

        elif self.voc_match(answer_situation, "help"):
            self.speak_dialog('protect.corona')

        else:
            self.speak("Ich konnte sie leider nicht verstehen", expect_response=False)
            
    @intent_file_handler('symptoms.coronavirus.intent')
    def handle_symptoms_coronavirus(self, message):
        self.speak_dialog('symptoms.coronavirus')
    
    @intent_file_handler('information.coronavirus.intent')
    def handle_information_coronavirus(self, message):
        self.speak_dialog('information.coronavirus')

    @intent_file_handler('shopping.info.corona.intent')
    def handle_shopping_coronavirus(self, message):
        self.speak_dialog('shopping.info.corona')
     
    @intent_file_handler('news.coronavirus.intent')
    def handle_news_coronavirus(self, message):
        self.speak_dialog('news.coronavirus')

def create_skill():
    return CoronavirusInfoSkill()
