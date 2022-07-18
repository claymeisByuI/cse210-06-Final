from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class SolveChallengerAction(Action):

    def __init__(self, audio_service):
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        challengers = cast.get_actors(CHALLENGER_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        for challenger in challengers:
            remaining_word = challenger.get_answered_word().get_value().strip()
            if remaining_word == "":
                sound = Sound(BOUNCE_SOUND)
                self._audio_service.play_sound(sound)
                points = challenger.get_points()
                stats.add_points(points)
                stats.completed_word()
                cast.remove_actor(CHALLENGER_GROUP, challenger)
                callback.on_next(NEXT_WORD)

