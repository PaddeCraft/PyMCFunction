from pymcfunction.update_specific_types.effect import Effect


class effect:
    def __init__(self, target: str = "@s") -> None:
        self.target = target

    def give(
        self,
        effect: Effect,
        seconds: int = None,
        amplifier: int = None,
        hideParticles: bool = None,
    ):
        return f"effect give {self.target} {effect.value}" + (
            " "
            + (
                str(seconds)
                + (
                    " "
                    + (
                        str(amplifier)
                        + (
                            " " + ("true" if hideParticles else "false")
                            if hideParticles != None
                            else ""
                        )
                    )
                    if amplifier
                    else ""
                )
            )
            if seconds
            else ""
        )

    def clear(self, effect: Effect = None) -> str:
        return f"effect clear {self.target}" + ((" " + effect.value) if effect else "")
