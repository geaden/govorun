#!/usr/bin/env python3
"""Govorun Slack Bot"""

from rtmbot.core import Plugin


class GovorunPlugin(Plugin):

    def process_message(self, data):
        if '<@U4L8YJB25>' in data['text']:
            self.outputs.append(
                [data['channel'], 'Птица-говорун отличается умом и '
                 'сообразительностью'])
