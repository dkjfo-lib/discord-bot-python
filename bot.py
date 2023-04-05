import discord
import responses
import os


async def send_message(message: discord.Message, user_message, is_private) -> str:
    try:
        response = await responses.handle_response(user_message)
        if is_private:
            await message.author.send(content=response.text, embed=response.embed, embeds=response.embeds)
        else:
            await message.channel.send(content=response.text, embed=response.embed, embeds=response.embeds)
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = os.getenv('DISCORD_BOT_TOKEN')
    PREFIX = os.getenv('DISCORD_BOT_PREFIX')
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message: discord.Message):
        # Make sure bot doesn't get stuck in an infinite loop
        if message.author == client.user or not message.content.startswith(PREFIX):
            return

        # Get data about the user
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        user_message = user_message[len(PREFIX):]
        # Debug printing
        print(f"{username} said: '{user_message}' ({channel})")
        print(message)

        # If the user message contains a '?' in front of the text, it becomes a private message
        if user_message[0] == '?':
            user_message = user_message[1:]  # [1:] Removes the '?'
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)
