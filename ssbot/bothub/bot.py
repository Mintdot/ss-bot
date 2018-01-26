# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)

from bothub_client.bot import BaseBot
from bothub_client.messages import Message

from .weather import get_coord
from .bus import bus_response


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
        location = event.get('location')

        if location:
            self.coord_message(location)
        elif message == '/start':
            self.start_message(event)
        elif message == '날씨':
            self.location_message(event)
        elif message == '버스':
            self.bus_message(event)
        elif message == '목록으로':
            self.start_message(event)
        elif message == '신용산역':
            data = '03561'
            self.bus_response(data)
        elif message == '삼각지역':
            data = '03567'
            self.bus_response(data)
        elif message == '녹사평역':
            data = ''
            self.bus_response(data)
        else:
            self.what_message(event)

    def start_message(self, event):
        start = Message(event).set_text('무엇을 도와드릴까요?') \
            .add_keyboard_button('날씨') \
            .add_keyboard_button('버스')

        self.send_message(start)

    def location_message(self, event):
        location = Message(event).set_text('현재 위치 전송') \
            .add_location_request('위치전송') \
            .add_keyboard_button('목록으로')

        self.send_message(location)

    def coord_message(self, location):
        lat = location['latitude']
        lon = location['longitude']
        app_id = '58d7d00ad2c80ae28b09f1ac57b5d894'
        weather = get_coord(lat, lon, app_id)

        self.send_message(weather)

    def bus_message(self, event):
        bus = Message(event).set_text('어디를 조회 할까요?') \
            .add_keyboard_button('신용산역') \
            .add_keyboard_button('삼각지역') \
            .add_keyboard_button('녹사평역') \
            .add_keyboard_button('목록으로')

        self.send_message(bus)

    def bus_response(self, data):
        response = bus_response(data)

        self.send_message(response)

    def what_message(self, event):
        user = event.get('sender')['name']

        what = "{}님이 무슨 말씀을 하시는지 잘 모르겠네요\n" \
               "\"/start\"라고 입력해주시면 제가 도와드릴게요.".format(user)

        self.send_message(what)
