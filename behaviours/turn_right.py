from .base import Behaviour
from .states import STOP, DRIVE_FORWARD, DRIVE_BACKWARD, TURN_LEFT, TURN_RIGHT
from pybricks.parameters import Color
import time

class TurnRight(Behaviour):
    def __init__(self, name, motors):
        Behaviour.__init__(self, name)
        self.currentangle = 500 # randomize between 45-135?
        self.speed = 500
        self.motors = motors
        self.doneTurn = False

    def update(self, detectedColour, detectedProximity):

        # when both motors are stopped, return to drive forward
        # if (self.motors[0].speed == 0 and self.motors[1].speed == 0):
        #     return DRIVE_FORWARD
        if (self.doneTurn):
            self.doneTurn = False
            return DRIVE_FORWARD

        return TURN_RIGHT

    def on_enter(self):
        # start running motor[0] at 500 degrees per second
        self.motors[0].run_angle(self.speed, -self.currentangle, wait=False)
        self.motors[1].run_angle(self.speed, self.currentangle, wait=False)

        time.sleep(2)

        self.doneTurn = True

    def on_exit(self):
        # stop the robot
        # iterate over motors
        for motor in self.motors:
            motor.brake()
