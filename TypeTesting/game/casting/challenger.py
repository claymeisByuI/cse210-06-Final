from constants import *
from game.casting.actor import Actor
from game.casting.point import Point
from game.casting.text import Text

class Challenger(Actor):
    """A implement Word to type in the game."""

    def __init__(self, wordText, answeredWordText, position = Point(), velocity = Point(), debug=True):
        """Constructs a new Challenger Word.

        Args:Args:
            body: A new instance of Body.
            animation: A new instance of Animation.
            word: the word of the challenge
            debug: If it is being debugged.
        """
        super().__init__(debug)
        self._word = wordText
        self._answeredWordText = answeredWordText
        self._position = position
        self._velocity = velocity

    def get_word(self):
        """Gets the label's text.

        Returns:
            An instance of Text.
        """
        return self._word

    def get_answered_word(self):
        """Gets the label's text.

        Returns:
            An instance of Text.
        """
        return self._answeredWordText

    def get_position(self):
        """Gets the label's position.

        Returns:
            An instance of Point.
        """
        return self._position

    def get_velocity(self):
        """Gets the label's position.

        Returns:
            An instance of Point.
        """
        return self._velocity

    def set_position(self, position):
        """Sets the position to the given value.

        Args:
            position: An instance of Point.
        """
        self._position = position

    def get_points(self):
        """
        Number of points the challenge is worth
        Returns:

        """
        return len(self._word.get_value())

    def move_next(self):
        """Moves the Challenger using its velocity."""
        new_position = self._position.add(self._velocity)
        self.set_position(new_position)

    def process_next_letter(self, keyboard_service):
        """
        Checks the next unanswered letter against the keyboard service
        Args:
            keyboard_service:

        Returns:

        """
        word = self._answeredWordText.get_value()
        for idx, char in enumerate(word):
            if char != " ":
                if keyboard_service.is_key_pressed(char):
                    self._answeredWordText.set_value(word[:idx] + " " + word[idx+1:])
                break



