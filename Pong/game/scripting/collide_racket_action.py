from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideRacketAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service

    def execute(self, cast, script, callback):

        ball = cast.get_first_actor(BALL_GROUP)

        racket1 = cast.get_first_actor(RACKET_GROUP1)

        racket2 = cast.get_first_actor(RACKET_GROUP2)

        ball_body = ball.get_body()
        racket_body1 = racket1.get_body()
        racket_body2 = racket2.get_body()

        if self._physics_service.has_collided(ball_body, racket_body1):
            ball.bounce_x()
            sound = Sound(BOUNCE_SOUND)
            self._audio_service.play_sound(sound)

        if self._physics_service.has_collided(ball_body, racket_body2):
            ball.bounce_x()
            sound = Sound(BOUNCE_SOUND)
            self._audio_service.play_sound(sound)
