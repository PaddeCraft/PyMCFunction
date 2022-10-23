from pymcfunction.types import Gamemode

def say(msg):
    return "say " + str(msg)


def function(path: str, includeWorkspace=True):
    return "function " + ("@@PYMCFUNCTION-NAMESPACE:" if includeWorkspace else "") + path

def clear(target:str="@s"):
    return "clear " + target

def defaultgamemode(mode:Gamemode):
    val = mode.value
    if val[0] == "!":
        raise Exception("Default gamemode needs to be one specific gamemode.")
    return "defaultgamemode " + val

def deop(player:str):
    return "deop " + player