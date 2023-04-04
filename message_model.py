import discord

class message_model:
    def __init__(
        self,
        text,
        embed
    ):
        self.text :str = text
        self.embed: discord.Embed = embed