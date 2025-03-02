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
        log.debug("[ENGINE] Turning left at"+str(percent)+"%")
        speed = speed
        percent = percent
        self.move.on(motor.SpeedPercent(percent), motor.SpeedPercent(speed))

    def hard_left(self, speed = SPEED):
        log.debug("[ENGINE] Turning left at"+str(speed)+"%")
        self.move.on(motor.SpeedPercent(-speed), motor.SpeedPercent(speed))

    def turn_right(self, percent = 50, speed = SPEED):
        log.debug("[ENGINE] Turning right at"+str(percent)+"%")
        speed = speed
        percent = percent
        self.move.on(motor.SpeedPercent(speed), motor.SpeedPercent(percent))

    def hard_right(self, speed = SPEED):
        log.debug("[ENGINE] Turning right at"+str(speed)+"%")
        speed = speed
        self.move.on(motor.SpeedPercent(speed), motor.SpeedPercent(-speed))


class LineFollowerSensors:
    def __init__(self, left, right):
        self.leftsensor = ColorSensor(left)
        self.rightsensor = ColorSensor(right)
        
        with open("colours.pickle", "rb") as f:
            self.cal = pickle.load(f)
        

        self.leftsensor.mode = "COL-COLOR"
        self.rightsensor.mode = "COL-COLOR"
    '''
    def left(self):
        reflected_light = self.leftsensor.reflected_light_intensity

        if reflected_light in range(40, 60): # dark green (22%)
            return "green"
        elif reflected_light in range(0, 25): # black (0%)
            return "black"
        elif reflected_light > 80: # white (100%)
            return "white"
    
    def right(self):
        reflected_light = self.rightsensor.reflected_light_intensity

        if reflected_light in range(40, 60): # dark green (22%)
            return "green"
        elif reflected_light in range(0, 25): # black (0%)
            return "black"
        elif reflected_light > 80: # white (100%)
            return "white"
    
    def left_raw(self):
        return self.leftsensor.reflected_light_intensity
    
    def right_raw(self):
        return self.rightsensor.reflected_light_intensity
            
    '''
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

    def right(self):
        colour = self.rightsensor.color
        if colour == 0: # No colour found
            return "None"
        elif colour == 1: # Black
            return "black"
        elif colour == 2: # Blue
            return "blue"
        elif colour == 3: # Green
            return "gree"
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

    def left2(self):
        raw = self.left_raw()

        if raw[0] in range(self.cal["black"]["min"][0], self.cal["black"]["max"][0]) and raw[1] in range(self.cal["black"]["min"][1], self.cal["black"]["max"][1]) and raw[2] in range(self.cal["black"]["min"][2], self.cal["black"]["max"][2]):
            return "black"
        elif raw[0] in range(self.cal["green"]["min"][0], self.cal["green"]["max"][0]) and raw[1] in range(self.cal["green"]["min"][1], self.cal["green"]["max"][1]) and raw[2] in range(self.cal["green"]["min"][2], self.cal["green"]["max"][2]):
            return "gree"
        elif raw[0] in range(self.cal["white"]["min"][0], self.cal["white"]["max"][0]) and raw[1] in range(self.cal["white"]["min"][1], self.cal["white"]["max"][1]) and raw[2] in range(self.cal["white"]["min"][2], self.cal["white"]["max"][2]):
            return "white"
        else:
            return "None"
        
    def right2(self):
        raw = self.right_raw()

        if raw[0] in range(self.cal["black"]["min"][0], self.cal["black"]["max"][0]) and raw[1] in range(self.cal["black"]["min"][1], self.cal["black"]["max"][1]) and raw[2] in range(self.cal["black"]["min"][2], self.cal["black"]["max"][2]):
            return "black"
        elif raw[0] in range(self.cal["green"]["min"][0], self.cal["green"]["max"][0]) and raw[1] in range(self.cal["green"]["min"][1], self.cal["green"]["max"][1]) and raw[2] in range(self.cal["green"]["min"][2], self.cal["green"]["max"][2]):
            return "gree"
        elif raw[0] in range(self.cal["white"]["min"][0], self.cal["white"]["max"][0]) and raw[1] in range(self.cal["white"]["min"][1], self.cal["white"]["max"][1]) and raw[2] in range(self.cal["white"]["min"][2], self.cal["white"]["max"][2]):
            return "white"
        else:
            return "None"


    