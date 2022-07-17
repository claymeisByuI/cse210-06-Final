from constants import *
from game.casting.actor import Actor


class Stats(Actor):
    """The game stats."""

    def __init__(self, debug = False):
        """Constructs a new Stats."""
        super().__init__(debug)
        self._level = 1
        self._speed = START_SPEED
        self._score = 0
        self._word_count = 0

    def completed_word(self):
        """
        increments current word count
        Returns:

        """
        self._word_count += 1

    def get_word_count(self):
        """
        gets the current word count
        Returns:

        """
        return self._word_count

    def add_points(self, points):
        """Adds the given points to the score.
        
        Args:
            points: A number representing the points to add.
        """
        self._score += points

    def get_speed(self):
        return self._speed

    def get_level(self):
        """Gets the level.

        Returns:
            A number representing the level.
        """
        return self._level

    def get_lives(self):
        """Gets the lives.

        Returns:
            A number representing the lives.
        """
        return self._lives
  
    def get_score(self):
        """Gets the score.

        Returns:
            A number representing the score.
        """
        return self._score

    def next_level(self):
        """Adds one level."""
        self._level += 1
        self._speed += 3


    def reset(self):
        """Resets the stats back to their default values."""
        self._level = 1
        self._speed = START_SPEED
        self._score = 0