from game.casting.color import Color

# GAME
GAME_NAME = "TypeTesting"
FRAME_RATE = 60
START_SPEED = 2

# SCREEN
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2


# HUD
HUD_MARGIN = 15
LEVEL_GROUP = "level"
WORDS_GROUP = "words"
SCORE_GROUP = "score"
LEVEL_FORMAT = "LEVEL: {}"
WORDS_FORMAT = "WORDS: {}"
SCORE_FORMAT = "SCORE: {}"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
NEXT_WORD = 4
GAME_OVER = 5

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# --------------------------------------------------------------------------------------------------
# CASTING CONSTANTS
# --------------------------------------------------------------------------------------------------

# STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 3
MAXIMUM_LIVES = 5



# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS SPACE TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME OVER"

# UI FONT
FONT_FILE = "TypeTesting/assets/fonts/zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48


# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# KEYS
LEFT = "left"
RIGHT = "right"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# SOUND
BOUNCE_SOUND = "TypeTesting/assets/sounds/boing.wav"
WELCOME_SOUND = "TypeTesting/assets/sounds/start.wav"
OVER_SOUND = "TypeTesting/assets/sounds/over.wav"

# CHALLENGER
CHALLENGER_GROUP = "challenger"

# CHALLENGER FONT
CHALLENGER_FONT_FILE = "TypeTesting/assets/fonts/UbuntuMono-Bold.ttf"
CHALLENGER_FONT_SIZE = 32

# CHALLENGER FONT ANSWERED
CHALLENGER_FONT_ANSWERED_FILE = "TypeTesting/assets/fonts/UbuntuMono-Regular.ttf"
CHALLENGER_FONT_ANSWERED_SIZE = 32

# WORDS
WORDS_FILE = "TypeTesting/assets/data/words.txt"
