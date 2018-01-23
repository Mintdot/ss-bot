# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)

from bothub_client.bot import BaseBot
from bothub_client.messages import Message


class Bot(BaseBot):
    """Represent a Bot logic which interacts with a user.

    BaseBot superclass have methods belows:

    * Send message
      * self.send_message(message, chat_id=None, channel=None)
    * Data Storage
      * self.set_project_data(data)
      * self.get_project_data()
      * self.set_user_data(data, user_id=None, channel=None)
      * self.get_user_data(user_id=None, channel=None)

    When you omit user_id and channel argument, it regarded as a user
    who triggered a bot.
    """

    def handle_message(self, event, context):
        message = event.get('content')
        if message == '/help':
            self.help_message(event)
        elif message == '날씨':
            self.weather_message(event)
        elif message == '버스':
            self.bus_message()
        else:
            self.what_message(event)

    def help_message(self, event):
        help = Message(event).set_text('무엇을 도와드릴까요?')\
            .add_keyboard_button('날씨')\
            .add_keyboard_button('버스')

        self.send_message(help)

    def weather_message(self, event):
        return

    def bus_message(self):
        return

    def what_message(self, event):
        member = event.get('sender')
        member_name = member['name']

        what = "{}님이 무슨 말씀을 하시는지 잘 모르겠네요\n" \
               "\"/help\"라고 입력해주시면 제가 도와드릴게요.".format(member_name)

        self.send_message(what)

