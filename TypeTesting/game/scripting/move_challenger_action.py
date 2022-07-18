from constants import *
from game.scripting.action import Action


class MoveChallengerAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        challengers = cast.get_actors(CHALLENGER_GROUP)
        for challenger in challengers:
            challenger.move_next()

