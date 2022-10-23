class team:
    def __init__(self, name: str) -> None:
        self.name = name

    def create(self, displayName: str = None):
        return f"team add {self.name}" + ((" " + displayName) if displayName else "")

    def listTeams(self):
        return "team list"

    def listMembers(self):
        return "team list " + self.name

    def remove(self):
        return "team remove " + self.name

    def empty(self):
        return "team emtpy " + self.name

    def join(self, target: str = "@s"):
        return f"team join {self.name} {target}"

    def leave(self, target: str):
        return f"team leave {target}"

    def modify(self, option: str, value: str):
        return f"team modify {self.name} {option} {value}"
