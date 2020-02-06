"""A tiny bot with sole purpose of deleting all messages 
that contain certaing phrases from the server."""

import discord 
from discord.ext import commands

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or('% '), 
    сase_insensitive=True
)
        
@bot.event
async def on_ready():
    print(f"{bot.user} online")

@bot.event 
async def on_command_error(ctx, error):
    await ctx.message.add_reaction("✋")
    embed = discord.Embed(title='Error', description=error)
    if ctx.command.description:
        embed.add_field(name="Command help", value=ctx.command.description)
    await ctx.send(embed=embed)

@bot.event 
async def on_command_completion(ctx, error):
    await ctx.message.add_reaction("👌")

@commands.has_permissions(administrator=True)
@bot.command(
    description='% purge <any amount of phrases, each in its own quotes> - iterates over the whole server and deletes any messages that contain any of the lookup phrases. Only server admins can use the command.'
)
async def purge(ctx, *, phrases):
    phrases = [i.lower() for i in phrases]
    for channel in ctx.guild.text_channels:
        async for message in channel.history(limit=1000000000):
            if any(( i in message.content.lower() for i in phrases)):
                await message.delete()

bot.run('TOKEN'')