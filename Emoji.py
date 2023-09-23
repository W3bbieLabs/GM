from random import choice
class Emoji():
	def __init__( self ):
		self.emojis = [ '🍄','🦧','🌎','🕴🏽','👀','🎅🏾','🔥','🤯','💅🏾','🍕','🦾','😂','☺️','🤬','🙄','😈','🤠','🤡','👾','💀','🙏🏾','🧠','🌞','☀️','🐔','🥶','💩', '💀','🆘','☠️','🏴‍☠️', '🔗', '😳', '🦷', '🧛🏼‍♂️', '💃🏻','💃🏼','💃🏽','💃🏾','💃🏿','👙','🦺','👘','🥽','🌂','🦊','🐸','🐝','🦄' ]
		self.current_emoji = ''
	def add( self, emoji_to_add ):
		self.emojis.append( emoji_to_add )
	def get(self):
		return choice( self.emojis )
	def view( self ):
		print( 'emojis:', self.emojis )
	def set(self, current_emoji):
		self.current_emoji = current_emoji
		return self.current_emoji