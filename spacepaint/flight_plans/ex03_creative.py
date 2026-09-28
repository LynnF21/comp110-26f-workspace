"""Arrange the components of my scene"""

__author__: str = "731001286"

from math import atan2, degrees, sqrt

from spacepaint import Ship, start_spacepaint


def angle_between(ship: Ship, x: float, y: float) -> float:
    """Return the shortest signed turn toward an X/Y waypoint."""
    difference: float = degrees(atan2(y - ship.y, x - ship.x)) - ship.heading_x_y

    if difference > 180.0:
        difference -= 360.0
    elif difference < -180.0:
        difference += 360.0

    return difference


def distance_between(ship: Ship, x: float, y: float) -> float:
    """Compute the distance from the ship to an X/Y point."""
    return sqrt((x - ship.x) ** 2 + (y - ship.y) ** 2)


def move_to(ship: Ship, x: float, y: float) -> None:
    """Move ship using the shortest turn possible"""
    turn_amount: float = angle_between(ship, x, y)
    distance: float = distance_between(ship, x, y)

    ship.turn(turn_amount)
    ship.forward(distance)

    return None


def draw_moon(ship: Ship, x: float, y: float) -> None:
    """Paint a yellow moon"""
    ship.beam(on=False)
    ship.fill(on=False)

    move_to(ship, x, y)

    ship.beam_color(value="yellow")
    ship.beam(on=True)
    ship.fill(on=True)

    ship.arc(radius=1.0, degrees=360.0)

    ship.beam(on=False)

    return None


def draw_door(ship: Ship, x: float, y: float) -> None:
    """Paint a barn door in red in the corner of the barn"""
    width: float = 2.0
    height: float = 2.0

    ship.beam(on=False)
    ship.fill(on=False)

    move_to(ship, x, y)

    ship.beam_color(value="red")
    ship.beam_width(width=0.05)

    ship.fill(on=True, opacity=0.5)
    ship.beam(on=True)

    move_to(ship, x + width, y)
    move_to(ship, x + width, y + height)
    move_to(ship, x, y + height)
    move_to(ship, x, y)

    ship.fill(on=False)
    ship.beam(on=False)

    return None


def draw_barn(ship: Ship, x: float, y: float) -> None:
    """Paint a barn in the corner of the cordinate plane"""
    width: float = 6.0
    wall_height: float = 4.0
    roof_height: float = 3.0

    left_x: float = x
    right_x: float = x + width
    middle_x: float = x + width / 2.0

    bottom_y: float = y
    wall_top_y: float = y + wall_height
    roof_top_y: float = wall_top_y + roof_height

    ship.beam(on=False)
    ship.fill(on=False)

    move_to(ship, left_x, bottom_y)

    ship.beam_color(value="red")
    ship.beam_width(width=0.1)
    ship.fill(on=True, opacity=0.5)
    ship.beam(on=True)

    move_to(ship, right_x, bottom_y)
    move_to(ship, right_x, wall_top_y)
    move_to(ship, middle_x, roof_top_y)
    move_to(ship, left_x, wall_top_y)
    move_to(ship, left_x, bottom_y)

    ship.fill(on=False)
    ship.beam(on=False)

    draw_door(ship, x + 2.0, y)

    return None


def draw_tree(ship: Ship, x: float, y: float, size: float) -> None:
    """Paint a tree"""
    trunk_width: float = size
    trunk_height: float = size
    crown_height: float = size
    crown_width: float = size

    ship.beam(on=False)
    ship.fill(on=False)

    move_to(ship, x - trunk_width / 2, y)

    ship.beam_color(value="green")
    ship.fill(on=True)
    ship.beam(on=False)

    left_x: float = x - crown_width / 2.0
    right_x: float = x + crown_width / 2.0
    top_y: float = y + trunk_height + crown_height
    crown_bottom_y: float = y + trunk_height

    move_to(ship, left_x, crown_bottom_y)
    ship.beam(on=True)
    move_to(ship, right_x, crown_bottom_y)
    move_to(ship, x, top_y)
    move_to(ship, left_x, crown_bottom_y)

    return None


def square_at(ship: Ship, center_x: float, center_y: float, length: float) -> None:
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
    """Paint the picture"""
    aura.speed(multiplier=4.0)

    draw_barn(aura, 7.0, 0)
    draw_moon(aura, 1.0, 11.0)

    tree_x: float = -5.0
    tree_count: int = 0

    while tree_count < 3:
        draw_tree(aura, tree_x, -2.0, 2.0)
        tree_x += 3.0
        tree_count += 1

    return None


if __name__ == "__main__":
    start_spacepaint()
