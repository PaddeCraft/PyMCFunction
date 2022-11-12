from enum import Enum
from .update_specific_types.advancement import Advancement
from .update_specific_types.effect import Effect
from .update_specific_types.entity import Entity
from .update_specific_types.block import Block
from .update_specific_types.item import Item


class Gamemode(Enum):
    ADVENTURE = "adventure"
    CREATIVE = "creative"
    SPECTATOR = "spectator"
    SURVIVAL = "survival"
    NOT_ADVENTURE = "!adventure"
    NOT_CREATIVE = "!creative"
    NOT_SPECTATOR = "!spectator"
    NOT_SURVIVAL = "!survival"


class SortOrder(Enum):
    ARBITRARY = "arbitrary"
    FURTHEST = "furthest"
    NEAREST = "nearest"
    RANDOM = "random"


class DataType(Enum):
    BLOCK = "block"
    ENTITY = "entity"
    STORAGE = "storage"


class AnchorType(Enum):
    EYES = "eyes"
    FEET = "feet"


class Dimension(Enum):
    OVERWORLD = "minecraft:overworld"
    NETHER = "minecraft:the_nether"
    END = "minecraft:the_end"


class StoreType(Enum):
    RESULT = "result"
    SUCCESS = "success"


class StoreDataType(Enum):
    BYTE = "byte"
    SHORT = "short"
    INT = "int"
    LONG = "long"
    FLOAT = "float"
    DOUBLE = "double"


class StoreBossbarPosition(Enum):
    VALUE = "value"
    MAX = "max"


class ScoreboardRenderType(Enum):
    HEARTS = "hearts"
    INTEGER = "integer"


class Weather(Enum):
    CLEAR = "clear"
    RAIN = "rain"
    THUNDER = "thunder"


class ContainerType(Enum):
    ENTITY = "entity"
    BLOCK = "block"


class BanListType(Enum):
    PLAYERS = "players"
    IPS = "ips"


class BossbarGetType(Enum):
    MAX = "max"
    PLAYERS = "players"
    VALUE = "value"
    VISIBLE = "visible"


class BossbarColor(Enum):
    BLUE = "blue"
    GREEN = "green"
    PINK = "pink"
    PURPLE = "purple"
    RED = "red"
    WHITE = "white"
    YELLOW = "yellow"


class BossbarStyle(Enum):
    NOTCHED6 = "notched_6"
    NOTCHED10 = "notched_10"
    NOTCHED12 = "notched_12"
    NOTCHED20 = "notched_20"
    PROGRESS = "progress"


class Difficultiy(Enum):
    PEACEFUL = "peaceful"
    EASY = "easy"
    NORMAL = "normal"
    HARD = "hard"


class ExperienceUnit(Enum):
    LEVELS = "levels"
    POINTS = "points"


class TimeQueryType(Enum):
    DAYTIME = "daytime"
    GAMETIME = "gametime"
    DAY = "day"


class TimePreset(Enum):
    DAY = "day"
    NIGHT = "night"
    NOON = "noon"
    MIDNIGHT = "midnight"
