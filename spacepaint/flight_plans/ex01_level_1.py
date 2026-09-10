"""Making art... in space!"""

from spacepaint import Ship, start_spacepaint

__author__: str = "731001286"


def square(ship: Ship) -> None:
    """Paint a square from the ships origin point"""
    ship.turn(degrees=90.0)
    ship.forward(units=6.0)
    ship.turn(degrees=90.0)
    ship.forward(units=6.0)
    ship.turn(degrees=90.0)
    ship.forward(units=6.0)
    ship.turn(degrees=90.0)
    ship.forward(units=6.0)
    ship.turn(degrees=90.0)
    return None


def main(aura: Ship) -> None:
    """Painting four equal in length squares."""
    aura.beam(on=True)
    square(ship=aura)
    square(ship=aura)
    square(ship=aura)
    square(ship=aura)
    return None


if __name__ == "__main__":
    start_spacepaint()
