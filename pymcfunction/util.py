import json

from .types import *


def _dictToMcKeyVal(d: dict):
    return json.dumps(d).replace('"', "").replace("'", "").replace(" ", "")


def selector(
    type: str,
    advancemens: dict = None,
    distance: str | int = None,
    dx: float | int = None,
    dy: float | int = None,
    dz: float | int = None,
    gamemode: Gamemode = None,
    level: str | int = None,
    limit: int = None,
    name: str = None,
    nbt: dict = None,
    scores: dict = None,
    sort: SortOrder = None,
    tags: str | list[str] = None,
    team: str = None,
    entityType: Entity = None,
    x: float | int = None,
    y: float | int = None,
    z: float | int = None,
    x_rotation: float | int = None,
    y_rotation: float | int = None,
):
    things = []
    if advancemens:
        things.append("advancements=" + _dictToMcKeyVal(advancemens))
    if distance:
        things.append("distance=" + distance)
    if dx:
        things.append("dx=" + str(dx))
    if dy:
        things.append("dy=" + str(dy))
    if dz:
        things.append("dz=" + str(dz))
    if gamemode:
        things.append("gamemode=" + gamemode.value)
    if level:
        things.append("level=" + str(level))
    if limit:
        things.append("limit=" + str(limit))
    if name:
        things.append("name=" + name)
    if nbt:
        things.append("nbt=" + _dictToMcKeyVal(nbt))
    if scores:
        things.append("scores=" + _dictToMcKeyVal(scores))
    if sort:
        things.append("sort=" + sort.value)
    if tags:
        if type(tags) == str:
            things.append("tag=" + tags)
        else:
            for t in tags:
                things.append("tag=" + t)
    if team:
        things.append("team=" + team)
    if entityType:
        things.append("type=" + entityType.value)
    if x:
        things.append("x=" + x)
    if y:
        things.append("y=" + y)
    if z:
        things.append("z=" + z)
    if x_rotation:
        things.append("x_rotation=" + x_rotation)
    if y_rotation:
        things.append("y_rotation=" + y_rotation)

    if len(things) >= 1:
        return type + "[" + ",".join(things) + "]"
    return type
