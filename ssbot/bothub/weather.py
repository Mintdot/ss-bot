import requests

base_url = 'http://api.openweathermap.org/data/2.5/weather'


def get_coord(lat, lon, app_id): # 좌표 받아오기
    url = '{}?lat={}&lon={}&APPID={}'.format(base_url, lat, lon, app_id)
    response = requests.get(url)  # 데이터 긁어오기
    data = response.json()  # 딕셔너리 타입으로 변환

    name = data.get('name')
    kelvin = 273.15
    temp = data.get('main')
    temp_average = temp['temp'] - kelvin
    temp_min = temp['temp_min'] - kelvin
    temp_max = temp['temp_max'] - kelvin
    humidity = temp['humidity']

    message = "[{}의 날씨]\n" \
              "평균 기온: {}℃\n" \
              "최저 기온: {}℃\n" \
              "최고 기온: {}℃\n" \
              "습도: {}%".format(name, temp_average, temp_min, temp_max, humidity)

    return message
