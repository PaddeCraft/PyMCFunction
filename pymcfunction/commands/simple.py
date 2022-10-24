from types import NoneType
from pymcfunction.types import BanListType, Difficultiy, Gamemode, Weather
from pymcfunction.update_specific_types.block import Block
from pymcfunction.update_specific_types.entity import Entity
from pymcfunction.update_specific_types.item import Item
from pymcfunction.util import _dictToMcKeyVal


def say(msg: str):
    return "say " + str(msg)


def function(path: str, includeWorkspace=True):
    return (
        "function " + ("@@PYMCFUNCTION-NAMESPACE:" if includeWorkspace else "") + path
    )


def clear(target: str = "@s"):
    return "clear " + target


def defaultgamemode(mode: Gamemode):
    val = mode.value
    if val[0] == "!":
        raise Exception("Default gamemode needs to be one specific gamemode.")
    return "defaultgamemode " + val


def deop(player: str):
    return "deop " + player


def op(player: str):
    return "op " + player


def stop():
    return "stop"


def weather(_type: Weather, duration: int = 999999):
    return f"weather {_type.value} {duration}"


def seed():
    return "seed"


def setworldspawn(coord: str, yaw: float = 0.0):
    return f"setworldspawn {coord} {yaw}"


def setidletimeout(minutes: int):
    return "setidletimeout " + str(minutes)


def give(target: str, item: Item | Block, count: int = 1):
    return f"give {target} {item.value} {count}"


def kill(target: str):
    return "kill " + target


def kick(target: str):
    return "kick " + target


def gamemode(mode: Gamemode):
    val = mode.value
    if val[0] == "!":
        raise Exception("Gamemode needs to be one specific gamemode.")
    return "gamemode " + val


def gamerule(rule: str, val: str):
    return f"gamerule {rule} {val}"


def save_all(flush=False):
    return "save-all" + (" flush" if flush else "")


def save_off():
    return "save-off"


def save_on():
    return "save-on"


def ban(player: str, reason: str = None):
    return f"ban {player}" + ((" " + reason) if reason else "")


def ban_ip(ip: str, reason: str = None):
    return f"ban-ip {ip}" + ((" " + reason) if reason else "")


def pardon(player: str):
    return "pardon " + player


def pardon_ip(ip: str):
    return "pardon " + ip


def teammsg(msg: str):
    return "teammsg " + msg


def banlist(_type: BanListType):
    return "banlist " + _type.value


def summon(entity: Entity, pos: str = "~ ~ ~", nbt: dict | str = None):
    return f"summon {entity.value} {pos}" + (
        ((" " + (_dictToMcKeyVal(nbt)) if type(nbt) == dict else nbt)) if nbt else ""
    )


def stopsound(target: str, source: str = None, sound: str = None):
    return f"stopsound {target}" + (
        (" " + (source + ((" " + sound) if sound else ""))) if source else ""
    )


def spectate(target: str | NoneType, spectator: str = "@s"):
    if target:
        return f"spectate {target} {spectator}"
    return "spectate"


def spawnpoint(target: str, coord: str = "~ ~ ~", yaw: float = None):
    return f"spawnpoint {target} {coord}" + ((" " + yaw) if yaw else "")


def difficulty(_difficulty: Difficultiy):
    return "difficulty " + _difficulty.value
