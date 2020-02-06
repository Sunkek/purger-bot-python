# purger-bot-python
A tiny bot with sole purpose of deleting all messages that contain certain phrases from a Discord server.

## Requirements

Python 3.7+

Python module ["discord.py"](https://discordpy.readthedocs.io/en/latest/intro.html#installing)

## Setup

- Obtain the bot token at https://discordapp.com/developers/applications/

- Put your bot token in the last line of main.py instead of `TOKEN`

- Run the file with Python3.7+.

- Add the bot to your server.

## Usage

`% purge <any amount of phrases, each in its own quotes>` 

The bot iterates over the whole server and deletes any messages that contain any of the lookup phrases. 
Case-insensitive. Only server admins can use the command.

Example of usage: 
`% purge "nagger" "nugger" "nogger"`

Careful with short phrases, uless you want to remove 90% of your server messages and possibly get your bot banned for Discord API abuse.
