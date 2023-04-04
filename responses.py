import discord
from message_model import message_model 
import weather


async def handle_response(message) -> message_model:
    p_message = message.lower()
    if p_message == 'weather':
        return await weather.get_weather('Belgrade')
    if p_message == 'test':
        return await weather.get_weather_test('Belgrade')

    else:
        return "<module 'sex with mishka' from kostroma city is no corrected>"