"""Self-driving robotic race car controller level 2."""

from racing import RobotCommand, RobotSensors

__author__: str = "731001286"

RACING_NAME: str = "Level 2"
RACING_COLOR: str = "#000080"


def control(sensors: RobotSensors) -> RobotCommand:
    """Control cars throttle based by speed"""

    throttle: float = (15.0 - sensors.odometry.speed_mps) / 15.0
    steer: float = 0.0

    if sensors.wall_lidar.front_left_m < 6.0:
        steer = 1.0
    elif sensors.wall_lidar.front_right_m < 6.0:
        steer = -1.0
    else:
        steer = 0.0

    return RobotCommand(throttle=throttle, steer=steer)
