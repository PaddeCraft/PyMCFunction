from pymcfunction.types import ContainerType
from pymcfunction.update_specific_types.block import Block
from pymcfunction.update_specific_types.item import Item


class item:
    def __init__(self) -> None:
        pass

    def modifyEntity(self, target: str, slot: str, modifier: str):
        return f"item modify entity {target} {slot} {modifier}"

    def modifyBlock(self, coord: str, slot: str, modifier: str):
        return f"item modify block {coord} {slot} {modifier}"

    def replaceEntity(self, target: str, slot: str, item: Item | Block, count: int = 1):
        return f"item replace entity {target} {slot} with {item.vale} {count}"

    def replaceBlock(self, coord: str, slot: str, item: Item | Block, count: int = 1):
        return f"item replace block {coord} {slot} with {item.value} {count}"

    def copy(
        self,
        sourceType: ContainerType,
        source: str,
        sourceSlot: str,
        destType: ContainerType,
        dest: str,
        destSlot: str,
        modifier: str = None,
    ):
        """Copy item

        Args:
            sourceType (ContainerType): ContainerType.ENTITY or ContainerType.Block
            source (str): Coordinate or selector of source
            sourceSlot (str): Slot of item in the source
            destType (ContainerType): ContainerType.ENTITY or ContainerType.BLOCK
            dest (str): Coordinate or selector of destination
            destSlot (str): Slot of item in destination
        """
        return f"item replace {destType.value} {dest} {destSlot} from {sourceType.value} {source} {sourceSlot}{(' ' + modifier) if modifier else ''}"
