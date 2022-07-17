from constants import *
from game.scripting.action import Action


class MoveChallengerAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        challengers = cast.get_actors(CHALLENGER_GROUP)
        for challenger in challengers:
            challenger.move_next()
            if challenger.get_position().get_x() < 0:
                print("Game ending")
                callback.on_next(GAME_OVER)
