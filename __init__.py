from mycroft import MycroftSkill, intent_file_handler


class JanuaryAnnouncement(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('announcement.january.intent')
    def handle_announcement_january(self, message):
        self.speak_dialog('announcement.january')


def create_skill():
    return JanuaryAnnouncement()

