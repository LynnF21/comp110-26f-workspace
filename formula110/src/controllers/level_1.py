"""Self-driving robotic race car controller level 0."""

from racing import RobotCommand, RobotSensors

__author__: str = "731001286"

RACING_NAME: str = "Level 1"
RACING_COLOR: str = "#000080"


def control(sensors: RobotSensors) -> RobotCommand:
    """Control car at a max speed."""

    throttle: float = 0.0
    steer: float = 0.0

    if sensors.wall_lidar.front_left_m < 4.0:
        steer = 1.0
    elif sensors.wall_lidar.front_right_m < 4.0:
        steer = -1.0
    else:
        steer = 0.0

    if sensors.odometry.speed_mps < 10.0:
        throttle = 0.20
    else:
        throttle = 0.05

    return RobotCommand(throttle=throttle, steer=steer)
