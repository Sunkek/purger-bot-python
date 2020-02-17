"""A tiny bot with sole purpose of deleting all messages 
that contain certaing phrases from the server."""

import discord 
from discord.ext import commands
from typing import Optional

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
    embed = discord.Embed(title='Error', description=str(error))
    if ctx.command.description:
        embed.add_field(name="Command help", value=ctx.command.description)
    await ctx.send(embed=embed)

@bot.event 
async def on_command_completion(ctx, error):
    await ctx.message.add_reaction("👌")

@commands.has_permissions(administrator=True)
@bot.command(
    name='purgebyphrases',
    aliases=['pbp'],
    description='% purgebyphrases <optional start channel ID or mention> <any amount of phrases, each in its own quotes> - iterates over the whole server from top to bottom and deletes any messages that contain any of the lookup phrases. If you need to purge down from some specific channel, mention that channel as the first argument. Only server admins can use the command.'
)
async def purgebyphrases(
    ctx, 
    channel: Optional[discord.TextChannel]=None, 
    *phrases
):
    phrases = [i.lower() for i in phrases]
    if channel:
        channels = [
            i for i in ctx.guild.text_channels 
            if i.position >= channel.position
        ]
    else:
        channels = ctx.guild.text_channels
    counter = 0
    for channel in channels:
        print(channel.name)
        async for message in channel.history(limit=1000000000):
            counter += 1
            if counter % 1000 == 0:
                print(f'Messages checked: {counter}')
            if any((i in message.content.lower() for i in phrases)):
                print(message.author)
                print(message.content)
                await message.delete()

@commands.has_permissions(administrator=True)
@bot.command(
    name='purgebyauthors',
    aliases=['pba'],
    description='% purgebyauthors <optional start channel ID or mention> <any amount of user IDs or mentions> - iterates over the whole server from top to bottom and deletes any messages that were sent by any of the specified users. If you need to purge down from some specific channel, mention that channel as the first argument. Only server admins can use the command.'
)
async def purgebyauthors(
    ctx, 
    channel: Optional[discord.TextChannel]=None, 
    authors: commands.Greedy[discord.User]=[]
):
    print(authors)
    if channel:
        channels = [
            i for i in ctx.guild.text_channels 
            if i.position >= channel.position
        ]
    else:
        channels = ctx.guild.text_channels
    counter = 0
    for channel in channels:
        print(channel.name)
        async for message in channel.history(limit=1000000000):
            counter += 1
            if counter % 1000 == 0:
                print(f'Messages checked: {counter}')
            if message.author in authors:
                print(message.author)
                print(message.content)
                await message.delete()

bot.run('TOKEN')