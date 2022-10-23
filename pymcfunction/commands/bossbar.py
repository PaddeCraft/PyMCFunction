import re
from pymcfunction.types import BossbarColor, BossbarGetType, BossbarStyle


class bossbar:
    def __init__(self, id: str):
        self.id = id

    def create(self, name: str):
        return f"bossbar add {self.id} {name}"

    def get(self, propertie: BossbarGetType):
        return f"bossbar get {self.id} {propertie.value}"

    def listAll(self):
        return f"bossbar list"

    def setColor(self, color: BossbarColor):
        return f"bossbar set {self.id} color {color.value}"

    def setMax(self, max: int):
        return f"bossbar set {self.id} max {max}"

    def setName(self, name: str):
        return f"bossbar set {self.id} name {name}"

    def setPlayers(self, target: str):
        return f"bossbar set {self.id} players {target}"

    def setStyle(self, style: BossbarStyle):
        return f"bossbar set {self.id} style {style.value}"

    def setValue(self, value):
        return f"bossbar set {self.id} value {value}"

    def setVisibility(self, visible: bool):
        return f"bossbar set {self.id} visible " + ("true" if visible else "false")
