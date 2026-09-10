"""Making art... in space!"""

from spacepaint import Ship, start_spacepaint

__author__: str = "731001286"


def main(aura: Ship) -> None:
    """Your Space Paint program's entrypoint."""
    aura.turn(degrees=45.0)
    aura.forward(units=4.2426)
    aura.beam(on=True)
    aura.turn(degrees=135.0)
    aura.forward(units=6.0)
    aura.turn(degrees=90.0)
    aura.forward(units=6.0)
    aura.turn(degrees=90.0)
    aura.forward(units=6.0)
    aura.turn(degrees=90.0)
    aura.forward(units=6.0)
    return None


if __name__ == "__main__":
    start_spacepaint()
