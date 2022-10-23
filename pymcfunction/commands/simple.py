from pymcfunction.types import Gamemode, Weather


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


def give(target: str, item: str, count: int = 1):
    return f"give {target} {count}"


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
