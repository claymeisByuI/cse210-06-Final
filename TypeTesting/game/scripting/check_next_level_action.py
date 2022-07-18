from constants import *
from game.scripting.action import Action


class CheckNextLevelAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        stats = cast.get_first_actor(STATS_GROUP)
        challengers = cast.get_actors(CHALLENGER_GROUP)
        if len(challengers) == 0 and stats.get_word_count() % 5 == 0:
            stats.next_level()
            callback.on_next(NEXT_LEVEL)
