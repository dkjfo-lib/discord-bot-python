import requests
from message_model import message_model 
import os
import discord


async def get_weather_test(city: str) -> discord.Embed:
    complete_url = f'https://api.open-meteo.com/v1/forecast?latitude=44.80&longitude=20.47&hourly=temperature_2m,relativehumidity_2m,apparent_temperature,precipitation_probability,precipitation,weathercode,windspeed_10m&daily=sunrise,sunset,uv_index_max,precipitation_sum&windspeed_unit=ms&start_date=2023-04-04&end_date=2023-04-05&timezone=auto'
    response = requests.get(complete_url)
    data = response.json()
    print ()
    print ()
    print (data)
    print ()
    print ()

    data_h = data["hourly"]
    measures_count = len(data_h["time"])
    embed = discord.Embed(title=f"Погода в {city}")
    for id in range(0, measures_count, 2):
        name = f'{data_h["time"][id][11:]} {get_weather_emoji_test(data_h["weathercode"][id])}'
        perception = f'{data_h["precipitation"][id]}'
        value = f'{round(data_h["temperature_2m"][id])}°C\n{round(data_h["windspeed_10m"][id])}m/s\n{perception}mm'
        embed.add_field(name=name, value=value, inline=True)
        
        # if (id + 1) % 6 == 0:
        #     embed.add_field(name='\u200B', value='\u200B', inline=False)

    return message_model(text= None, embed = embed)

async def get_weather(city: str) -> discord.Embed:
    API_KEY = os.getenv('OPEN_WEATHER_MAP_API')
    complete_url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric&cnt=9'
    response = requests.get(complete_url, params={'lang': 'ru'})
    x = response.json()
    print (x)
    
    embed = discord.Embed(title=f"Погода в {city}")
    for wt in x["list"]:
        name = f'{wt["dt_txt"][-9:-3]} {wt["weather"][0]["description"]} {get_weather_emoji(wt["weather"][0]["icon"])}'
        
        perception = '0 '
        if "rain" in wt:
            perception = f'{wt["rain"]["3h"]}💧'
        elif "snow" in wt:
            perception = f'{wt["snow"]["3h"]}❄'
        value = f'{round(wt["main"]["temp_min"])}-{round(wt["main"]["temp_max"])}°C    {round(wt["wind"]["speed"])}m/s    {perception}mm/3h'
        
        embed.add_field(name=name, value=value)
    return message_model(text= None, embed = embed)

def get_weather_emoji(icon:str) -> str:
    icon = icon[:-1]
    if icon == '1':
        return "☀"
    elif icon == '2':
        return "🌤"
    elif icon == '3':
        return "☁"
    elif icon == '4':
        return "🌥"
    elif icon == '9':
        return "🌧"
    elif icon == '10':
        return "🌧"
    elif icon == '11':
        return "🌩"
    elif icon == '13':
        return "🌨"
    elif icon == '50':
        return "🌫"
    else: 
        return icon

def get_weather_emoji_test(code:int) -> str:
    if code == 0:
        return "☀"
    elif code == 2:
        return "🌤"
    elif code == 2:
        return "🌥"
    elif code == 3:
        return "☁"
    elif code <= 48:
        return "🌫"
    elif code <= 55:
        return "🌧"
    elif code <= 57:
        return "🌨"
    elif code <= 65:
        return "🌧"
    elif code <= 77:
        return "🌨"
    elif code <= 82:
        return "🌧"
    elif code <= 86:
        return "🌨"
    elif code <= 99:
        return "🌩"
    else: 
        return code