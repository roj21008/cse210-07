from constants import *
from game.scripting.action import Action


class ControlRacketAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service

    def execute(self, cast, script, callback):

        racket1 = cast.get_first_actor(RACKET_GROUP1)

        if self._keyboard_service.is_key_down(LEFT1):
            racket1.swing_left(RACKET_VELOCITY1)
        elif self._keyboard_service.is_key_down(RIGHT1):
            racket1.swing_right(RACKET_VELOCITY1)
        else:
            racket1.stop_moving()

        racket2 = cast.get_first_actor(RACKET_GROUP2)

        if self._keyboard_service.is_key_down(LEFT2):
            racket2.swing_left(RACKET_VELOCITY2)
        elif self._keyboard_service.is_key_down(RIGHT2):
            racket2.swing_right(RACKET_VELOCITY2)
        else:
            racket2.stop_moving()
