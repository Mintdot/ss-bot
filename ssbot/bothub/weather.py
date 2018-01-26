# -*- coding: utf-8 -*-

import requests

base_url = 'http://api.openweathermap.org/data/2.5/weather'


def get_coord(lat, lon, app_id):  # 좌표 받아오기
    url = '{}?lat={}&lon={}&APPID={}'.format(base_url, lat, lon, app_id)
    response = requests.get(url)  # 데이터 긁어오기
    data = response.json()  # 딕셔너리 타입으로 변환
    name = data.get('name')
    main = data.get('main')
    temp = round(main['temp'] - 273.15, 2)
    humidity = main['humidity']
    weather = data.get('weather')
    description = weather[0]['description']

    message = "[{}의 날씨]\n" \
              "현재 날씨: {}\n" \
              "현재 기온: {}℃\n" \
              "습도: {}%\n".format(name, description, temp, humidity)

    return message
