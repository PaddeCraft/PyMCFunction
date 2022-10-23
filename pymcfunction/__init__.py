__version__ = "0.1.5"

from .util import *

from .commands.tag import tag
from .commands.team import team
from .commands.item import item
from .commands.bossbar import bossbar
from .commands.execute import execute
from .commands.teleport import teleport
from .commands.scoreboard import Scoreboard

from .commands.simple import *


# Aliases
sb = Scoreboard
exec = execute
gm = gamemode
tp = teleport
bb = bossbar