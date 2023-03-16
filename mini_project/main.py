#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
ev3.speaker.say("Let's go!")

# Initialize motors.
right_motor = Motor(Port.B)
left_motor = Motor(Port.C)
# shoot_motor = Motor(Port.D)

#initailize sensors.
color_sensor = ColorSensor(Port.S2)
IR_sensor = InfraredSensor(Port.S3)

while(1):
    right_motor.run(2000)
    left_motor.run(2000)
    if color_sensor.color() == Color.BLACK:
        ev3.speaker.beep()
        right_motor.run_time(-5000, 1800, Stop.BRAKE, False)
        left_motor.run_time(-5000, 1800, Stop.BRAKE, True)
