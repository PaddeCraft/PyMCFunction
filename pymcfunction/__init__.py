__version__ = "0.1.6"

from .util import *

from .commands.tag import tag
from .commands.time import time
from .commands.team import team
from .commands.item import item
from .commands.effect import effect
from .commands.bossbar import bossbar
from .commands.execute import execute
from .commands.teleport import teleport
from .commands.experience import experience
from .commands.scoreboard import Scoreboard

from .commands.simple import *


# Aliases
sb = Scoreboard
xp = experience
exec = execute
gm = gamemode
tp = teleport
bb = bossbar
