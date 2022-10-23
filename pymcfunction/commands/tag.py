class tag:
    def __init__(self, target: str) -> None:
        self.target = target

    def add(self, tag):
        return f"tag {self.target} add {tag}"

    def remove(self, tag):
        return f"tag {self.target} remove {tag}"

    def list(self):
        return f"tag {self.target} list"
