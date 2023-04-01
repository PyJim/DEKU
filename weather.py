import requests, json

API_KEY = '9b442424160782fce6819aa7630b8fdb'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?q='

def getWeatherData(city):
    completeURL = BASE_URL + city + "&appid=" + API_KEY
    response = requests.get(completeURL)
    data = response.json()
    current_temperature = data["main"]["temp"]
    weather = data['weather'][0]["description"]

    text = f'The weather is {weather} at a temperature of {current_temperature} in {city}'
    return text
print(getWeatherData("Accra"))


