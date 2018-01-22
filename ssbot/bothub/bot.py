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
        if message == '/start':
            self.start_message(event)
        elif message == '안녕':
            self.hello_message(event)

    def start_message(self, event):
        start = Message(event).set_text('시작')\
            .add_keyboard_button('1번')\
            .add_keyboard_button('2번')

        self.send_message(start)

    def hello_message(self, event):
        me = event.get('sender')
        self.send_message('{}님 안녕하세요.'.format(me['name']))