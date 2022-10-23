from pymcfunction.types import AnchorType


class teleport:
    def __init__(self, target: str = "@s") -> None:
        self.target = target

    def destination(self, coord: str, rotation: float | int = None):
        return f"teleport {self.target} {coord}" + (
            (" " + str(rotation)) if rotation else ""
        )

    def facingCoordinate(self, coord: str, facing: str):
        return f"teleport {self.target} {coord} facing {facing}"

    def facingEntity(
        self, coord: str, facingEntity: str, anchor: AnchorType = AnchorType.EYES
    ):
        return f"teleport {self.target} {coord} facing entity {facingEntity} {anchor.value}"
