# -*- coding: utf-8 -*-

import requests

base_url = 'http://api.openweathermap.org/data/2.5/weather'


def get_coord(lat, lon, app_id):  # 좌표 받아오기
    url = '{}?lat={}&lon={}&APPID={}'.format(base_url, lat, lon, app_id)
    response = requests.get(url)  # 데이터 긁어오기
    data = response.json()  # 딕셔너리 타입으로 변환

    name = data.get('name')
    main = data.get('main')
    temp = main['temp'] - 273.15  # 절대 온도로 불러오기 때문에 273.15만큼 빼줘야 섭씨 온도를 구할 수 있다.
    humidity = main['humidity']

    message = "[{}의 날씨]\n" \
              "기온: {}℃\n" \
              "습도: {}%".format(name, temp, humidity)

    return message
