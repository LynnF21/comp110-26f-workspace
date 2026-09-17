"""Self-driving robotic race car controller level 3."""

from racing import RobotCommand, RobotSensors

__author__: str = "731001286"

RACING_NAME: str = "Level 3"
RACING_COLOR: str = "#000080"


def control(sensors: RobotSensors) -> RobotCommand:
    """Control car with camera sensor"""

    throttle: float = (15.0 - sensors.odometry.speed_mps) / 2.0
    steer: float = 0.0

    if sensors.camera.heading_error_degrees > 0.5:
        steer = 0.5
    elif sensors.camera.heading_error_degrees < -0.5:
        steer = -0.5
    else:
        steer = 0.0

    return RobotCommand(throttle=throttle, steer=steer)
