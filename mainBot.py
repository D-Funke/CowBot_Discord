"""
Author(s): D-Funke
Last Modified: 11/11/2022
𝄞♭
"""

import discord
import random
import os

from discord.ext import commands
from _resources.constants import GUILD_TOKEN_ID, BOT_TOKEN_ID, LOCK_STRING

def GetCowSayQuotes(filename: str):
    phraseList = []
    try:
        with open(filename, 'r') as fptr:
            lineData = fptr.readline().replace("\n", "")
            while(lineData != ""):
                if(lineData.__contains__('<StartPhrase>')):
                    tempString = ""
                elif(lineData.__contains__('<EndPhrase>')):
                    phraseList.append(tempString)
                else:
                    tempString += lineData+"\n"
                lineData = fptr.readline().replace("\n", "")
    except FileNotFoundError:
        print(f'File \"{os.getcwd()}\{filename}\" does not exist or unable to be opened\n')
    except:
        print('Unexpected Error\n')
    return phraseList

class CowBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        _intents = discord.Intents.all()
        _intents.members = True
        self.phraseList = GetCowSayQuotes("_resources/cowBotQuotes.txt")
        super().__init__(command_prefix='!', intents=_intents, *args, **kwargs)

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content == "cowsay":
            response = random.choice(self.phraseList)
            print(response)
            await message.channel.send(response)

if __name__ == "__main__":
    # Debugging Code Execution Section
    """
    print(os.getcwd())
    printList = GetCowSayQuotes("_resources\cowBotQuotes.txt")
    print(random.choice(printList))
    """

    # Main Bot Code Execution Section
    cowSayBot = CowBot()
    cowSayBot.run(BOT_TOKEN_ID)
    