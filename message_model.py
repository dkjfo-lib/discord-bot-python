from ast import List
import discord

class message_model:
    def __init__(
        self,
        text = None,
        embed = None,
        embeds = None
    ):
        self.text :str = text
        self.embed: discord.Embed = embed
        self.embeds: List[discord.Embed] = embeds