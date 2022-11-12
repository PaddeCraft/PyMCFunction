from pymcfunction.types import ExperienceUnit


class experience:
    def __init__(self, selector: str = "@s") -> None:
        self.selector = selector

    def add(self, anmount: int, unit: ExperienceUnit):
        return f"xp add {self.selector} {anmount} {unit.value}"

    def remove(self, anmount: int, unit: ExperienceUnit):
        # xp remove is not an actual command in the game,
        # but uses xp add with a negative anmount
        return self.add(anmount * -1, unit)

    def query(self, unit: ExperienceUnit):
        return f"xp query {self.target} {unit.value}"

    def set(self, anmount, unit: ExperienceUnit):
        return f"xp set {self.selector} {anmount} {unit.value}"
