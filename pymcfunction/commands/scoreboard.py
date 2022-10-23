from pymcfunction.types import ScoreboardRenderType


class Scoreboard:
    def __init__(self, name: str, type: str = "dummy") -> None:
        self.name = name
        self.type = type

    def create(self):
        return f"scoreboard objectives add {self.name} {self.type}"

    def delete(self):
        return f"scoreboard objectives remove {self.name}"

    def setdisplay(self, slot: str):
        return f"scoreboard objectives setdisplay {slot} {self.name}"

    def modifyDisplayName(self, displayNameJsonComponent: str | dict):
        return f"scoreboard objectives modify {self.name} displayname {displayNameJsonComponent}"

    def modifyRendertype(self, rendertype: ScoreboardRenderType):
        return f"scoreboard objectives modify {self.name} rendertype {rendertype.value}"

    def __getitem__(self, target: str) -> str:
        return f"scoreboard players get {target} {self.name}"

    def __setitem__(self, target: str, value: int) -> str:
        return f"scoreboard players set {target} {self.name} {value}"

    def add(self, target: str, score: int):
        return f"scoreboard players add {target} {self.name} {score}"

    def remove(self, target: str, score: int):
        return f"scoreboard players remove {target} {self.name} {score}"

    def reset(self, target: str):
        return f"scoreboard players reset {target} {self.name}"

    def enable(self, target: str):
        return f"scoreboard players enable {target} {self.name}"

    def operation(
        self,
        target: str,
        targetObjective: str,
        operation: str,
        source: str,
        sourceObjective: str,
    ):
        return f"scoreboard players operation {target} {targetObjective} {operation} {source} {sourceObjective}"
