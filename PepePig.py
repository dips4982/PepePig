# bot.py
import os
import asyncio
import discord.file
import typing
from dotenv import load_dotenv
import discord
from discord.ext import commands
from discord.utils import get
from googletrans import Translator, LANGCODES

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# class HelpCog(commands.Cog):
#     # def get_command_signature(self, command):
#     #     return '{0.clean_prefix}{1.qualified_name} - {1.signature}'.format(self, command)
#     @commands.command(name = 'help')
#     async def help(self, ctx):
#         await ctx.send("FINNALLYYYYYYY BITCH ASS")


pepe = commands.Bot(command_prefix='pepe ')#, help_command=MyHelpCommand())

@pepe.event
async def on_ready():
    print(f'{pepe.user} has connected to Discord!')
    game = discord.Game(name = "with ur mum")
    await pepe.change_presence(activity=game)

@pepe.event
async def on_message(message):
    if message.author == pepe.user:
        return
    
    Babu = pepe.get_user(707545525960048670)
    if Babu and message.author == Babu:
        await message.channel.send(f"{Babu.mention}, babu please maa chuda lol. I'm not interested yaar mujhe sunna hi nahi hai")
        return
    
    msg = message.content
    if msg.lower().startswith('ayy') and msg.lower().endswith('y'):
        await message.channel.send(f'lmao {message.author.mention}')
    elif "who" in msg.lower() and "daddy" in msg.lower():
        Rishi = pepe.get_user(425968693424685056)
        await message.channel.send(f'{Rishi.mention} is my daddy. {pepe.cogs}')

    await pepe.process_commands(message)

# class HelpCog(commands.Cog):
#     def __init__(self, bot):
#         self.bot = bot
#         self._original_help_command = bot.help_command
#         bot.help_command = MyHelpCommand()
#         bot.help_command.cog = self
    
#     def cog_unload(self):
#         self.bot.help_command = self._original_help_command

class PepeTasks(commands.Cog):
    """
    Contains first year tasks for bot-ragging purposes.
    """
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(
    pass_context=True, 
    name = 'giveintro',
    help = "- Gives intro in various languages like a good first year boi."
    )
    async def giveintro(self, ctx):
        msg = ctx.message
        words = msg.content.split(' ')
        
        intro_text = "I'm Pepe Pig (**cRoaK**).\nThis is my little brother George (**mEeP mEeP**),\nthis is mummy pig (**bruh sound effect #2**),\nand this is DADDY FROG (**huge snort**)"
        
        # LANGCODES has keys as languages, values as codes
        try:
            code = LANGCODES[words[2]]
            await ctx.send(f"detected langcode: {code}")
            fp = open("media\pepevideo_trim.mp4", "rb")
            video = discord.File(fp, filename="intro.mp4")
            # await ctx.send(file=video) # uncomment to send the intro vid
            
            trans = Translator()
            translated_intro = trans.translate(intro_text, dest=code)
            await ctx.send(translated_intro.text)#, tts=True)
            if code == "es":
                fp = open("media\spanishsound.mp3", "rb")
                sound = discord.File(fp, filename="spanish sound.mp3")
                await ctx.send(file=sound)
            elif code == "hi":
                fp = open("media\hindisound.mp3", "rb")
                sound = discord.File(fp, filename="hindi sound.mp3")
                await ctx.send(file=sound)
        except:
            await ctx.send("Enter a valid language you dumbass!" +
            "\nSyntax: pepe giveintro <language name>")

    @commands.command(
    pass_context=True, 
    name = 'languages',
    help = "- Lists all supported languages for intro"
    )
    async def languages(self, ctx):
        text = [(lang, code) for lang, code in LANGCODES.items()]
        await ctx.send('\n'.join([f"{code}: {lang}" for code, lang in text]))
    

class UtilityCommands(commands.Cog):
    """ 
    Contains some useful commands (lmao jk)
    """
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(
    pass_context=True, 
    name = 'clear',
    help = "- Clears the n most recent messages from (optional) specific user or all users"
    )
    async def clear(self, ctx, user: typing.Optional[discord.Member], number: typing.Optional[int] = 1):
        if user is None:
            deleted = await ctx.channel.purge(limit=number+1)
            await ctx.send('{} deleted the last {} message(s) lol. Ab tu suspense me hi mar'.format(ctx.message.author.name, number))
        else:
            count = 0
            to_delete = []

            if user.id == ctx.message.author.id: number += 1

            async for message in ctx.channel.history(): #default limit 100
                if count == number:
                    break
                if message.author.id == user.id:
                    to_delete.append(message)
                    count += 1

            await ctx.channel.delete_messages(to_delete)
            await ctx.send('{} deleted the last {} message(s) from user {} lol. Ab tu suspense me hi mar'.format(ctx.message.author.name, number, user.display_name))#+'\n'.join([i.content for i in to_delete]))

def setup(pepe):
    pepe.remove_command('help')
    pepe.add_cog(PepeTasks(pepe))
    pepe.add_cog(UtilityCommands(pepe))
    # pepe.add_cog(HelpCog(pepe))

setup(pepe)
pepe.run(TOKEN)
pepe.clear()