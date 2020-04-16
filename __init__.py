from mycroft import MycroftSkill, intent_file_handler, intent_handler
from mycroft.util import play_mp3

class CoronavirusInfoSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.learning = True
        
    @intent_file_handler('situation.coronavirus.intent')
    def handle_situation_coronavirus(self, message):
        #self.speak_dialog('situation.coronavirus')
        answer_situation = self.get_response('situation.coronavirus')
        
        if "nachrichten" or "neuigkeiten" in answer_situation:
            self.speak("Okay, ich spiele die neuen Nachrichten von Ö3 zu dem Coronavirus")
            play_mp3("https://oe3meta.orf.at/oe3mdata/StaticAudio/Nachrichten.mp3")
            
        elif "einkaufen" in answer_situation:
            answer_einkaufen = self.get_response("Möchtest du etwas zur empfohlenen Einkaufszeit wissen?")
            
            if "ja" in answer_einkaufen:
                self.speak("Okay, folgendes:")
                self.speak_dialog('shopping.info.corona')
            
            else:
                answer_anders = self.get_response("Möchtest du vielleicht noch etwas anderwes wissen?")
                    
                    if "ja" in answer_anders:
                        answer_anders2 = self.get_response("Und was genau? Nachrichten? Symptome? Schutz?")
                        
                        if "nachrichten" or "neugikeiten" in answer_anders2:
                            self.speak("Okay, ich spiele die neuen Nachrichten von Ö3 zu dem Coronavirus")
                            play_mp3("https://oe3meta.orf.at/oe3mdata/StaticAudio/Nachrichten.mp3")
                            
                        elif "symptome" or "anzeichen" in answer_anders2:
                            self.speak_dialog('symptomps.info.corona')
                        
                        elif "schutz" or "hilfe" in answer_anders2:
                            self.speak_dialog('protection.corona')
                        
                        else:
                            self.speak("Okay, danke ich bin gerne für dich da", expect_response=False)
                    
                elif "nein" in answer_anders:
                    self.speak("Okay, danke ich bin gerne für dich da", expect_response=False)
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
