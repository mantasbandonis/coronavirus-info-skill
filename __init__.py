from mycroft import MycroftSkill, intent_file_handler


class CoronavirusInfo(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('info.coronavirus.intent')
    def handle_info_coronavirus(self, message):
        self.speak_dialog('info.coronavirus')


def create_skill():
    return CoronavirusInfo()

