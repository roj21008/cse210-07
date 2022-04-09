from game.casting.color import Color

# --------------------------------------------------------------------------------------------------
# GENERAL GAME CONSTANTS
# --------------------------------------------------------------------------------------------------

# GAME
GAME_NAME = "Pong"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "Pong/assets/fonts/zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
BOUNCE_SOUND = "Pong/assets/sounds/boing.wav"
WELCOME_SOUND = "Pong/assets/sounds/start.wav"
OVER_SOUND = "Pong/assets/sounds/over.wav"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)
RED = Color(255, 0, 0)


# KEYS
LEFT1 = "up"
RIGHT1 = "down"
LEFT2 = "w"
RIGHT2 = "s"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_GAME = 2
IN_PLAY = 3
GAME_OVER1 = 4
GAME_OVER2 = 5

# --------------------------------------------------------------------------------------------------
# SCRIPTING CONSTANTS
# --------------------------------------------------------------------------------------------------

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
STATS_GROUP_1 = "stats1"
STATS_GROUP_2 = "stats2"
DEFAULT_LIVES = 3
MAXIMUM_LIVES = 5

# HUD
HUD_MARGIN = 15
LIVES_GROUP_2 = "live"
LIVES_GROUP = "lives"
SCORE_GROUP = "score"
LIVES_2_FORMAT = "LIVES: {}"
LIVES_FORMAT = "Player 2 LIVES: {}"
LIVES_FORMAT2 = "Player 1 LIVES: {}"
SCORE_FORMAT = "SCORE: {}"

# BALL
BALL_GROUP = "balls"
BALL_IMAGE = "Pong/assets/images/000.png"
BALL_WIDTH = 28
BALL_HEIGHT = 28
BALL_VELOCITY = 6

# RACKET
RACKET_GROUP1 = "rackets1"
RACKET_GROUP2 = 'rackets2'
RACKET_IMAGES1 = [f"Pong/assets/images/{n:03}.png" for n in range(100, 103)]
RACKET_IMAGES2 = [f"Pong/assets/images/{n:03}.png" for n in range(103, 106)]
RACKET_WIDTH = 28
RACKET_HEIGHT = 106
RACKET_RATE = 6
RACKET_VELOCITY1 = 7
RACKET_VELOCITY2 = 7


# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME_1 = "GAME OVER\nPLAYER 1 WINS"
WAS_GOOD_GAME_2 = "GAME OVER\nPLAYER 2 WINS"
