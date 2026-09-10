"""Making art... in space!"""

from spacepaint import Ship, start_spacepaint

__author__: str = "731001286"


def square(ship: Ship, length: float) -> None:
    """Paint a square from the ships origin point"""
    ship.turn(degrees=90.0)
    ship.forward(units=length)
    ship.turn(degrees=90.0)
    ship.forward(units=length)
    ship.turn(degrees=90.0)
    ship.forward(units=length)
    ship.turn(degrees=90.0)
    ship.forward(units=length)
    ship.turn(degrees=90.0)
    return None


def main(aura: Ship) -> None:
    """Painting four squares of unequal lengths"""
    aura.beam(on=True)
    square(ship=aura, length=1.0)
    square(ship=aura, length=2.0)
    square(ship=aura, length=3.0)
    square(ship=aura, length=4.0)
    return None


if __name__ == "__main__":
    start_spacepaint()
