from pymcfunction.types import *
from .scoreboard import Scoreboard


class execute:
    def __init__(self, currentQuery="execute ") -> None:
        self.currentQuery = currentQuery

    def asEntity(self, target: str):
        self.currentQuery += f"as {target} "
        return self

    def atEntity(self, target: str):
        self.currentQuery += f"at {target} "
        return self

    def ifBlock(self, coord: str, block: Block):
        self.currentQuery += f"if block {coord} {block.value} "
        return self

    def ifBlocks(self, coord1: str, coord2: str, matchcoord: str, masked: bool = True):
        self.currentQuery += (
            f"if blocks {coord1} {coord2} {matchcoord} {'masked' if masked else 'all'} "
        )
        return self

    def ifPredicate(self, predicate: str):
        self.currentQuery += f"if predicate {predicate} "
        return self

    def ifData(self, _type: DataType, source: str, path: str):
        self.currentQuery += f"if data {_type.value} {source} {path} "
        return self

    def ifEntity(self, target: str):
        self.currentQuery += f"if entity {target} "

    def ifScoreMatches(self, target: str, scoreboard: Scoreboard, range: str):
        self.currentQuery += f"if score {target} {scoreboard.name} matches {range} "
        return self

    def ifScoreCompared(
        self,
        selector1: str,
        scoreboard1: Scoreboard,
        operator: str,
        selector2: str,
        scoreboard2: Scoreboard,
    ):
        self.currentQuery += f"if score {selector1} {scoreboard1.name} {operator} {selector2} {scoreboard2.name} "
        return self

    def unlessBlock(self, coord: str, block: Block):
        self.currentQuery += f"unless block {coord} {block.value} "
        return self

    def unlessBlocks(
        self, coord1: str, coord2: str, matchcoord: str, masked: bool = True
    ):
        self.currentQuery += f"unless blocks {coord1} {coord2} {matchcoord} {'masked' if masked else 'all'} "
        return self

    def unlessPredicate(self, predicate: str):
        self.currentQuery += f"unless predicate {predicate} "
        return self

    def unlessData(self, _type: DataType, source: str, path: str):
        self.currentQuery += f"unless data {_type.value} {source} {path} "
        return self

    def unlessEntity(self, target: str):
        self.currentQuery += f"unless entity {target} "

    def unlessScoreMatches(self, target: str, scoreboard: Scoreboard, range: str):
        self.currentQuery += f"unless score {target} {scoreboard.name} matches {range} "
        return self

    def unlessScoreCompared(
        self,
        selector1: str,
        scoreboard1: Scoreboard,
        operator: str,
        selector2: str,
        scoreboard2: Scoreboard,
    ):
        self.currentQuery += f"unless score {selector1} {scoreboard1.name} {operator} {selector2} {scoreboard2.name} "
        return self

    def align(self, axes: str):
        self.currentQuery += f"align {axes} "
        return self

    def anchored(self, anchor: AnchorType):
        self.currentQuery += f"anchored {anchor.value} "
        return self

    def facingCoord(self, coord: str):
        self.currentQuery += f"facing {coord} "
        return self

    def facingEntity(self, target: str, anchor: AnchorType):
        self.currentQuery += f"facing entity {target} {anchor.value} "
        return self

    def inDimension(self, dimension: Dimension):
        self.currentQuery += f"in {dimension.value} "
        return self

    def positioned(self, coord: str):
        self.currentQuery += f"positioned {coord} "
        return self

    def positionedAs(self, target: str):
        self.currentQuery += f"positioned as {target} "
        return self

    def rotated(self, yaw: float, pitch: float):
        self.currentQuery += f"rotated {yaw} {pitch} "
        return self

    def rotatedAs(self, target: str):
        self.currentQuery += f"rotated as {target} "
        return self

    def storeBlock(
        self,
        _type: StoreType,
        coord: str,
        path: str,
        storeDataType: StoreDataType,
        scale: float,
    ):
        self.currentQuery += f"store {_type.value} block {coord} {path} {storeDataType} {round(scale, 2)} "
        return self

    def storeBossbar(
        self, _type: StoreType, id: str | int, value: StoreBossbarPosition
    ):
        self.currentQuery += f"store {_type.value} bossbar {id} {value.value} "
        return self

    def storeEntity(
        self,
        _type: StoreType,
        target: str,
        path: str,
        storeDataType: StoreDataType,
        scale: float,
    ):
        self.currentQuery += f"store {_type.value} entity {target} {path} {storeDataType} {round(scale, 2)}"
        return self

    def storeScore(self, _type: StoreType, target: str, scoreboard: Scoreboard):
        self.currentQuery += f"store {_type.value} score {target} {scoreboard.name} "
        return self

    def storeStorage(
        self,
        _type: StoreType,
        id: str | int,
        path: str,
        storeDataType: StoreDataType,
        scale: float,
    ):
        self.currentQuery += f"store {_type.value} storage {id} {path} {storeDataType} {round(scale, 2)} "
        return self

    def run(self, *commands: str):
        return "\n".join((self.currentQuery + "run " + command) for command in commands)
