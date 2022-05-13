import json
import sqlite3
import requests

city = input('Enter name of the city: ')
key = '37e15cbe0fbff445c0b7704ce5e99bdb'
data = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric')

print(data.headers)
print(data.status_code)
print(data.url)
print(data.text)
api_data = data.json()
print(api_data)

with open('data.json', 'w') as file:
    json.dump(api_data, file, indent=4)
print(file)

temp_city = (api_data['main']['temp'])
pressure = api_data['main']['pressure']
humidity = api_data['main']['humidity']
wind_speed = api_data['wind']['speed']

print('Temperature: {:.2f} '.format(temp_city))
print('Pressure: ', pressure)
print('Humidity: ', humidity, '%')
print('Wind speed: ', wind_speed, 'km/ph')


conn = sqlite3.connect('database.sqlite')
cursor = conn.cursor()
cursor.execute(''' CREATE TABLE Weather(
                Temperature FLOAT,
                Pressure INT,
                Humidity INT,
                Wind speed FlOAT) ''')
cursor.execute("INSERT INTO Weather (Temperature, Pressure, Humidity, Wind) VALUES (?, ?, ?, ?)", (temp_city, pressure, humidity, wind_speed))
conn.commit()
conn.close()
