from WinxMusic.core.bot import WinxBot
from WinxMusic.core.dir import dirr
from WinxMusic.core.git import git
from WinxMusic.core.userbot import Userbot
from WinxMusic.misc import dbb, heroku, sudo
from .core.cookies import save_cookies

from .logging import LOGGER

# Directories
dirr()

# # Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()
# Bot Client
app = WinxBot()

# Assistant Client
userbot = Userbot()

from platforms import PlaTForms

Platform = PlaTForms()

HELPABLE = {}
