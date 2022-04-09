from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class MoveRacketAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        racket1 = cast.get_first_actor(RACKET_GROUP1)
        body1 = racket1.get_body()
        velocity1 = body1.get_velocity()
        position1 = body1.get_position()
        x1 = position1.get_y()

        position1 = position1.add(velocity1)

        if x1 < 0:
            position1 = Point(0, position1.get_x())
        elif x1 > (SCREEN_WIDTH - RACKET_WIDTH):
            position1 = Point(SCREEN_WIDTH - RACKET_WIDTH, position1.get_x())

        body1.set_position(position1)

        racket2 = cast.get_first_actor(RACKET_GROUP2)
        body2 = racket2.get_body()
        velocity2 = body2.get_velocity()
        position2 = body2.get_position()
        x2 = position2.get_y()

        position2 = position2.add(velocity2)

        if x2 < 0:
            position2 = Point(0, position2.get_x())
        elif x2 > (SCREEN_WIDTH - RACKET_WIDTH):
            position2 = Point(SCREEN_WIDTH - RACKET_WIDTH, position2.get_x())

        body2.set_position(position2)
