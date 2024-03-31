from UnxMusic.core.bot import Unx
from UnxMusic.core.dir import dirr
from UnxMusic.core.git import git
from UnxMusic.core.userbot import Userbot
from UnxMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Unx()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
