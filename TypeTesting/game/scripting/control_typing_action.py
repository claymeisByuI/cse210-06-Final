from constants import *
from game.scripting.action import Action


class ControlTypingAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        challengers = cast.get_actors(CHALLENGER_GROUP)
        for challenger in challengers:
            challenger.process_next_letter(self._keyboard_service);
