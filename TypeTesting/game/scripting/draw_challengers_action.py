from constants import *
from game.scripting.action import Action

class DrawChallengersAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        challengers = cast.get_actors(CHALLENGER_GROUP)
        for challenger in challengers:

            all_word = challenger.get_answered_word()
            position = challenger.get_position()
            self._video_service.draw_text(all_word, position)

            typed = challenger.get_word()
            position = challenger.get_position()
            self._video_service.draw_text(typed, position, Color(255, 255, 255, 100))
