from pymcfunction.types import TimePreset, TimeQueryType


class time:
    def __init__(self) -> None:
        pass

    def add(self, _time: int):
        return f"time add {_time}"

    def set(self, _time: int | TimePreset):
        return "time set " + (str(_time) if type(_time) == int else _time.value)

    def query(self, type: TimeQueryType):
        return f"time query {type.value}"
