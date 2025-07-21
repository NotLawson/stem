import ev3dev2.motor as motor
import ev3dev2.sensor as sensor
from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor

import time, json, pickle

if __name__ == "__main__":
    import log
    log.error("This file is not meant to be run as a standalone script")
    exit(1)

from __main__ import log
log.debug("[ROBOT] Loading Robot Library...")

class Engine:
    SPEED = 25
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.move = motor.MoveTank(left, right)

    def start(self, speed = SPEED):
        speed = speed
        log.debug("[ENGINE] Motor running at speed: " + str(speed))
        "Starts the motor at speed (default: 100%)"
        
        self.move.on(motor.SpeedPercent(speed), motor.SpeedPercent(speed))

    def stop(self):
        "Stops the motor"
        log.debug("[ENGINE] Motor stopped")
        self.move.off()

    def turn_left(self, percent = 50, speed = SPEED):
        log.debug("[ENGINE] Turning left at "+str(percent)+"%")
        speed = speed
        percent = percent
        self.move.on(motor.SpeedPercent(speed), motor.SpeedPercent(percent))

    def hard_left(self, speed = SPEED):
        log.debug("[ENGINE] Turning left at "+str(speed)+"%")
        self.move.on(motor.SpeedPercent(speed), motor.SpeedPercent(-speed))

    def turn_right(self, percent = 50, speed = SPEED):
        log.debug("[ENGINE] Turning right at "+str(percent)+"%")
        speed = speed
        percent = percent
        self.move.on(motor.SpeedPercent(percent), motor.SpeedPercent(speed))

    def hard_right(self, speed = SPEED):
        log.debug("[ENGINE] Turning right at "+str(speed)+"%")
        speed = speed
        self.move.on(motor.SpeedPercent(-speed), motor.SpeedPercent(speed))


class LineFollowerSensors:
    def __init__(self, left, right):
        self.leftsensor = ColorSensor(left)
        self.rightsensor = ColorSensor(right)

        self.leftsensor.mode = "COL-COLOR"
        self.rightsensor.mode = "COL-COLOR"

    def left(self):
        colour = self.leftsensor.color
        if colour == 0: # No colour found
            return "None"
        elif colour == 1: # Black
            return "black"
        elif colour == 2: # Blue
            return "blue"
        elif colour == 3: # Green
            return "green"
        elif colour == 4: # Yellow
            return "yellow"
        elif colour == 5: # Red
            return "red"
        elif colour == 6: # White
            return "white"
        elif colour == 7: # Brown
            return "brown"
        else: # lmao this should never pass
            return "string lmao"
    def left_raw(self):
        colour = self.leftsensor.raw
        return colour   

    def left_reflect(self):
        colour = self.leftsensor.reflected_light_intensity
        return colour     

    def right(self):
        colour = self.rightsensor.color
        if colour == 0: # No colour found
            return "None"
        elif colour == 1: # Black
            return "black"
        elif colour == 2: # Blue
            return "blue"
        elif colour == 3: # Green
            return "green"
        elif colour == 4: # Yellow
            return "Yellow"
        elif colour == 5: # Red
            return "red"
        elif colour == 6: # White
            return "white"
        elif colour == 7: # Brown
            return "brown"
        else: # lmao this should never pass
            return "string lmao"
    def right_raw(self):
        colour = self.rightsensor.raw
        return colour    

    def right_reflect(self):
        colour = self.rightsensor.reflected_light_intensity
        return colour


    