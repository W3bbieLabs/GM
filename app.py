''' system modules '''
import os 
import discord
from discord.ext import commands
from dotenv import load_dotenv
import random
import datetime

''' content modules '''
from Emoji import Emoji
from std_greetings import *
from units_of_time import *
from like_as_with import *
from to_begin import *
from emo_ingredients import *
from boondocks_char import *
from punc import *
from global_gm import *
from vee_gm import *
from non_us_gm import *
from boondocks_gm import *
from base_gm import *
from time_gm import *

''' server/guild setup '''
load_dotenv()
TOKEN = os.getenv( 'BOT_TOKEN' ) 
SERVER = os.getenv( 'SERVER_ID' )
LIVE_CHANNEL = os.getenv( 'GM_CHANNEL_ID' )
TEST_CHANNEL = os.getenv( 'TEST_CHANNEL' )

''' create client instance '''
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client( intents=intents )

# from Logger import Logger
# log = Logger()
# log.set_level()
# log.set_format()
# log.add_handler()

def response_types():
    ''' response types / syntax builds '''
    emoji = Emoji()

    response_types = [
    f'{ boondocks_gm( boondocks_characters) }', 
    f'{ vee_gm( emo_ingredients, like_as_with ) }',
    f'{ base_gm( emoji.get(), standard_greetings, punctuation, to_begin, like_as_with ) }',
    f'{ time_gm( units_of_time, like_as_with, emoji.get(), emo_ingredients ) }',
    f'{ global_gm( non_american_gm, emoji.get() ) }'
    ]
    return response_types

@client.event
async def on_ready():
    ''' bot is ready '''
    def gm_bot_self():
        ''' start message '''
        message = f'''gm_bot™\tbooting from terminal\ngoing to W3BBIE'''
        print(message); return message

    gm_bot_self()

@client.event
async def on_typing( channel, user, when ):
    ''' a user is typng in the thread, bot is listening '''
    message_author = user
    message_channel = channel
    print( user, "started to type in", channel, "on", when )

@client.event
async def on_message( message ):
    ''' when bot receives a message, applies to every message '''
    response = random.choice( response_types() )

    '''
    if message.author == client.user:
        # no response is message author is self 
          return
    '''
    early_morning = ( datetime.datetime.today().hour <= 8 and datetime.datetime.today().hour >= 1 )
    late_morning = ( datetime.datetime.today().hour <= 11 and datetime.datetime.today().hour >= 9 )
    early_afternoon = ( datetime.datetime.today().hour <= 14 and datetime.datetime.today().hour >= 12 )
    late_afternoon = ( datetime.datetime.today().hour <= 18 and datetime.datetime.today().hour >= 15 )
    early_evening = ( datetime.datetime.today().hour <= 21 and datetime.datetime.today().hour >= 19 )
    late_evening = ( datetime.datetime.today().hour <= 24 and datetime.datetime.today().hour >= 22 )
    # no_longer_morning = ( datetime.datetime.today().hour >= 11 )
    # proper_channel = ( message.channel == LIVE_CHANNEL )

    try:
        if early_morning:
            append_to_response = '`woah you are up early!`'
            response = f'{append_to_response} {response}'
        if late_morning:
            append_to_response = '`haha, did you hit the snooze button?`'
            response = f'{append_to_response} {response}'
        if early_afternoon:
            append_to_response = '`Shhheeeet, what up?`'
            response = f'{append_to_response} {response}'
        if late_afternoon:
            append_to_response = '`Almost toast time!`'
            response = f'{append_to_response} {response}'
        if early_evening:
            append_to_response = '`What yall got for dinner`'
            response = f'{append_to_response} {response}'
        if late_evening:
            append_to_response = 'Sweet dreams!'
            response = f'{append_to_response} {response}'
        # if no_longer_morning:
            # response = '`sorry, it is no longer morning. but glad you are here!`'
        
        if message.content.startswith( 'gm'.lower() ):
            ''' message uses lower casing '''
            await message.channel.send( content=response  )

        elif message.content.startswith( 'gm'.upper() ):
            ''' message using upper casing '''
            await message.channel.send( content=response )

        elif message.content.startswith('gm'.title() ):
            ''' message uses title casing '''
            await message.channel.send( content=response )
        
        elif message.content.startswith( 'morning' ):
            ''' message begins with no-gm word, morning '''
            await message.channel.send( content=response )

        elif message.content.startswith( 'todm'.lower() ):
            ''' message uses todm acronym '''
            await message.channel.send( content=response )

        elif message.content.startswith( 'todm'.upper() ):
            ''' message uses TODM acronym '''
            await message.channel.send( content=response )

        elif message.content.startswith( 'todm'.title() ):
            ''' message uses Todm acronym '''
            await message.channel.send( content=response )

        elif message.content.startswith( 'ga'.lower() ):
            ''' afternoon message uses lower casing '''
            await message.channel.send( content=response  )

        elif message.content.startswith( 'ga'.upper() ):
            ''' afternoon message using upper casing '''
            await message.channel.send( content=response )

        elif message.content.startswith('ga'.title() ):
            ''' afternoon message uses title casing '''
            await message.channel.send( content=response )

        elif message.content.startswith( 'toda'.lower() ):
            ''' message uses toda acronym '''
            await message.channel.send( content=response )

        elif message.content.startswith( 'toda'.upper() ):
            ''' message uses TODA acronym '''
            await message.channel.send( content=response )

        elif message.content.startswith( 'toda'.title() ):
            ''' message uses Toda acronym '''
            await message.channel.send( content=response )

        elif message.content.startswith( 'todn'.lower() ):
            ''' message uses todn acronym '''
            await message.channel.send( content=response )

        elif message.content.startswith( 'todn'.upper() ):
            ''' message uses TODN acronym '''
            await message.channel.send( content=response )

        elif message.content.startswith( 'todn'.title() ):
            ''' message uses Todn acronym '''
            await message.channel.send( content=response )

        elif message.content.startswith( 'gn'.lower() ):
            ''' message uses lower casing '''
            await message.channel.send( content=response  )

        elif message.content.startswith( 'gn'.upper() ):
            ''' message using upper casing '''
            await message.channel.send( content=response )

        elif message.content.startswith('gn'.title() ):
            ''' message uses title casing '''
            await message.channel.send( content=response )

        print( f'gm bot sent a reply to { message.channel }!' )

    except ValueError:
        print( 'invalid value passed.' )

    except TypeError:
        print( 'attempting to pass an invalid content type.' )

@client.event
async def on_disconnect():
    ''' bot has disconnected from the server '''
    print( f'gm bot booting down. see you next time.' )

''' run bot '''
client.run( TOKEN )
