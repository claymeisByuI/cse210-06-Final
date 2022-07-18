import csv
from constants import *
import random
from game.casting.stats import Stats
from game.casting.text import Text
from game.casting.label import Label
from game.casting.point import Point
from game.casting.challenger import Challenger

from game.scripting.initialize_devices_action import InitializeDevicesAction
from game.scripting.load_assets_action import LoadAssetsAction
from game.scripting.change_scene_action import ChangeSceneAction
from game.scripting.start_drawing_action import StartDrawingAction
from game.scripting.draw_hud_action import DrawHudAction
from game.scripting.draw_dialog_action import DrawDialogAction
from game.scripting.end_drawing_action import EndDrawingAction
from game.scripting.draw_challengers_action import DrawChallengersAction
from game.scripting.release_devices_action import ReleaseDevicesAction
from game.scripting.unload_assets_action import UnloadAssetsAction
from game.scripting.timed_change_scene_action import TimedChangeSceneAction
from game.scripting.play_sound_action import PlaySoundAction
from game.scripting.move_challenger_action import MoveChallengerAction
from game.scripting.control_typing_action import ControlTypingAction
from game.scripting.solve_challenger_action import SolveChallengerAction
from game.scripting.check_over_action import CheckOverAction
from game.scripting.check_next_level_action import CheckNextLevelAction
from game.services.raylib.raylib_audio_service import RaylibAudioService
from game.services.raylib.raylib_keyboard_service import RaylibKeyboardService
from game.services.raylib.raylib_physics_service import RaylibPhysicsService
from game.services.raylib.raylib_video_service import RaylibVideoService

class SceneManager:
    """The person in charge of setting up the cast and script for each scene."""

    AUDIO_SERVICE = RaylibAudioService()
    KEYBOARD_SERVICE = RaylibKeyboardService()
    PHYSICS_SERVICE = RaylibPhysicsService()
    VIDEO_SERVICE = RaylibVideoService(GAME_NAME, SCREEN_WIDTH, SCREEN_HEIGHT)

    INITIALIZE_DEVICES_ACTION = InitializeDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    LOAD_ASSETS_ACTION = LoadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)
    START_DRAWING_ACTION = StartDrawingAction(VIDEO_SERVICE)
    DRAW_HUD_ACTION = DrawHudAction(VIDEO_SERVICE)
    DRAW_DIALOG_ACTION = DrawDialogAction(VIDEO_SERVICE)
    END_DRAWING_ACTION = EndDrawingAction(VIDEO_SERVICE)
    DRAW_CHALLENGERS_ACTION = DrawChallengersAction(VIDEO_SERVICE)

    CONTROL_TYPING_ACTION = ControlTypingAction(KEYBOARD_SERVICE)
    MOVE_CHALLENGER_ACTION = MoveChallengerAction()
    SOLVE_CHALLENGER_ACTION = SolveChallengerAction(AUDIO_SERVICE)

    RELEASE_DEVICES_ACTION = ReleaseDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    UNLOAD_ASSETS_ACTION = UnloadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)
    CHECK_OVER_ACTION = CheckOverAction()
    CHECK_NEXT_LEVEL_ACTION = CheckNextLevelAction()

    ALL_WORDS = []

    def __init__(self):
        pass

    def prepare_scene(self, scene, cast, script):
        '''
        Prepares the game for playing
        Args:
            scene:
            cast:
            script:

        Returns:

        '''
        filename = WORDS_FILE
        with open(filename, 'r') as file:
            self.ALL_WORDS = file.readlines()


        if scene == NEW_GAME:
            self._prepare_new_game(cast, script)
        elif scene == NEXT_LEVEL:
            self._prepare_next_level(cast, script)
        elif scene == NEXT_WORD:
            self._prepare_next_word(cast, script)
        elif scene == IN_PLAY:
            self._prepare_in_play(cast, script)
        elif scene == GAME_OVER:
            self._prepare_game_over(cast, script)

    # ----------------------------------------------------------------------------------------------
    # scene methods
    # ----------------------------------------------------------------------------------------------

    def _prepare_new_game(self, cast, script):
        self._add_stats(cast)
        self._add_score(cast)
        self._add_words(cast)
        self._add_level(cast)

        self._add_dialog(cast, ENTER_TO_START)

        self._add_initialize_script(script)
        self._add_load_script(script)
        script.clear_actions(INPUT)
        script.add_action(INPUT, ChangeSceneAction(self.KEYBOARD_SERVICE, NEXT_LEVEL))
        self._add_output_script(script)
        self._add_unload_script(script)
        self._add_release_script(script)

    def _prepare_next_level(self, cast, script):
        print("Prepare next Level")
        self._add_dialog(cast, PREP_TO_LAUNCH)

        script.clear_actions(INPUT)
        script.add_action(OUTPUT, PlaySoundAction(self.AUDIO_SERVICE, WELCOME_SOUND))
        self._add_output_script(script)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 0))

    def _prepare_in_play(self, cast, script):
        cast.clear_actors(DIALOG_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        level = stats.get_level()
        for i in range(0, level):
            self._add_challenger(cast)

        script.clear_actions(INPUT)
        script.add_action(INPUT, self.CONTROL_TYPING_ACTION)
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_next_word(self, cast, script):
        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, .1))
        script.add_action(OUTPUT, PlaySoundAction(self.AUDIO_SERVICE, WELCOME_SOUND))

    def _prepare_game_over(self, cast, script):
        self._add_dialog(cast, WAS_GOOD_GAME)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(NEW_GAME, 5))
        script.clear_actions(UPDATE)
        self._add_output_script(script)

    # ----------------------------------------------------------------------------------------------
    # casting methods
    # ----------------------------------------------------------------------------------------------

    def _add_score(self, cast):
        cast.clear_actors(SCORE_GROUP)
        text = Text(SCORE_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(SCORE_GROUP, label)

    def _add_level(self, cast):
        cast.clear_actors(LEVEL_GROUP)
        text = Text(LEVEL_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_LEFT)
        position = Point(HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LEVEL_GROUP, label)

    def _add_words(self, cast):
        cast.clear_actors(WORDS_GROUP)
        text = Text(WORDS_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_RIGHT)
        position = Point(SCREEN_WIDTH - HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(WORDS_GROUP, label)

    def _add_stats(self, cast):
        cast.clear_actors(STATS_GROUP)
        stats = Stats()
        cast.add_actor(STATS_GROUP, stats)

    def _add_dialog(self, cast, message):
        cast.clear_actors(DIALOG_GROUP)
        text = Text(message, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, CENTER_Y)
        label = Label(text, position)
        cast.add_actor(DIALOG_GROUP, label)

    def _add_challenger(self, cast):
        cast.clear_actors(CHALLENGER_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        x = SCREEN_WIDTH
        y = SCREEN_HEIGHT /2
        position = Point(x, y)
        velocity = Point(stats.get_speed() * -1, 0)
        word = random.choice(self.ALL_WORDS)
        text = Text(word, CHALLENGER_FONT_ANSWERED_FILE, CHALLENGER_FONT_ANSWERED_SIZE, ALIGN_RIGHT)
        textAnswered = Text(word, CHALLENGER_FONT_FILE, CHALLENGER_FONT_SIZE, ALIGN_RIGHT)
        label = Challenger(text, textAnswered,  position, velocity)
        cast.add_actor(CHALLENGER_GROUP, label)

    # ----------------------------------------------------------------------------------------------
    # scripting methods
    # ----------------------------------------------------------------------------------------------
    def _add_initialize_script(self, script):
        script.clear_actions(INITIALIZE)
        script.add_action(INITIALIZE, self.INITIALIZE_DEVICES_ACTION)

    def _add_load_script(self, script):
        script.clear_actions(LOAD)
        script.add_action(LOAD, self.LOAD_ASSETS_ACTION)

    def _add_output_script(self, script):
        script.clear_actions(OUTPUT)
        script.add_action(OUTPUT, self.START_DRAWING_ACTION)
        script.add_action(OUTPUT, self.DRAW_HUD_ACTION)
        script.add_action(OUTPUT, self.DRAW_DIALOG_ACTION)
        script.add_action(OUTPUT, self.DRAW_CHALLENGERS_ACTION)
        script.add_action(OUTPUT, self.END_DRAWING_ACTION)

    def _add_release_script(self, script):
        script.clear_actions(RELEASE)
        script.add_action(RELEASE, self.RELEASE_DEVICES_ACTION)

    def _add_unload_script(self, script):
        script.clear_actions(UNLOAD)
        script.add_action(UNLOAD, self.UNLOAD_ASSETS_ACTION)

    def _add_update_script(self, script):
        script.clear_actions(UPDATE)
        script.add_action(UPDATE, self.MOVE_CHALLENGER_ACTION)
        script.add_action(UPDATE, self.SOLVE_CHALLENGER_ACTION)
        script.add_action(UPDATE, self.CHECK_OVER_ACTION)
        script.add_action(UPDATE, self.CHECK_NEXT_LEVEL_ACTION)

