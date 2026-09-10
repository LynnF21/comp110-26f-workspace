"""Making art... in space!"""

__author__: str = "731001286"

from math import atan2, degrees, sqrt

from spacepaint import Ship, start_spacepaint


def angle_between(ship: Ship, x: float, y: float) -> float:
    """Compute the turn from the ship's heading toward an X/Y point."""
    return degrees(atan2(y - ship.y, x - ship.x)) - ship.heading_x_y


def distance_between(ship: Ship, x: float, y: float) -> float:
    """Compute the distance from the ship to an X/Y point."""
    return sqrt((x - ship.x) ** 2 + (y - ship.y) ** 2)


def move_to(ship: Ship, x: float, y: float) -> None:
    """Move the ship from its current position to an X/Y point."""
    ship.turn(degrees(atan2(y - ship.y, x - ship.x)) - ship.heading_x_y)
    ship.forward(distance_between(ship, x, y))


def square_at(
    ship: Ship,
    center_x: float,
    center_y: float,
    length: float,
) -> None:
    """Paint a square center at an X/Y point."""
    half = length / 2

    upper_right_x = center_x + half
    upper_right_y = center_y + half
    upper_left_x = center_x - half
    upper_left_y = center_y + half
    lower_left_x = center_x - half
    lower_left_y = center_y - half
    lower_right_x = center_x + half
    lower_right_y = center_y - half

    ship.beam(on=False)
    move_to(ship, upper_right_x, upper_right_y)

    ship.beam(on=True)
    move_to(ship, upper_left_x, upper_left_y)
    move_to(ship, lower_left_x, lower_left_y)
    move_to(ship, lower_right_x, lower_right_y)
    move_to(ship, upper_right_x, upper_right_y)


def main(aura: Ship) -> None:
    """Painting five squares of unequal lengths"""
    aura.beam(on=True)
    square_at(ship=aura, center_x=0.0, center_y=0.0, length=5.0)
    square_at(ship=aura, center_x=0.0, center_y=0.0, length=4.0)
    square_at(ship=aura, center_x=0.0, center_y=0.0, length=3.0)
    square_at(ship=aura, center_x=0.0, center_y=0.0, length=2.0)
    square_at(ship=aura, center_x=0.0, center_y=0.0, length=1.0)
    return None


if __name__ == "__main__":
    start_spacepaint()
