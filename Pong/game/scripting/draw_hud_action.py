from constants import *
from game.scripting.action import Action


class DrawHudAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service

    def execute(self, cast, script, callback):
        stats_1 = cast.get_first_actor(STATS_GROUP_1)
        stats_2 = cast.get_first_actor(STATS_GROUP_2)

        self._draw_label(cast, LIVES_GROUP_2,
                         LIVES_FORMAT2, stats_2.get_lives())
        self._draw_label(cast, LIVES_GROUP, LIVES_FORMAT, stats_1.get_lives())

    def _draw_label(self, cast, group, format_str, data):
        the_value_to_display = format_str.format(data)
        label = cast.get_first_actor(group)
        text = label.get_text()
        text.set_value(the_value_to_display)
        position = label.get_position()
        self._video_service.draw_text(text, position)
