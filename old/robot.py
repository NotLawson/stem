import logging, time, json
log = logging.getLogger()
log.info("Loading Robot...")
import ev3dev2.motor as motor
import ev3dev2.sensor as sensor
from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor
from ev3dev2.sound import Sound

class Engine:
    SPEED = 17
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.move = motor.MoveTank(left, right, motor_class=motor.MediumMotor)
    def start(self, speed = SPEED):
        "Starts the motor at speed (default: 100%)"
        self.move.on(motor.SpeedPercent(speed), motor.SpeedPercent(-speed))
    def stop(self):
        "Stops the motor"
        self.move.off()
    def turn_left(self, percent = -SPEED, speed = SPEED):
        self.move.on(motor.SpeedPercent(percent), motor.SpeedPercent(-speed))
    def hard_left(self, percent = -SPEED):
        self.move.on(motor.SpeedPercent(percent), motor.SpeedPercent(percent))

    def turn_right(self, percent = -SPEED, speed = SPEED):
        self.move.on(motor.SpeedPercent(speed), motor.SpeedPercent(-percent))
    def hard_right(self, percent = -SPEED):
        self.move.on(motor.SpeedPercent(-percent), motor.SpeedPercent(-percent))

class Sensors:
    def __init__(self, left, right):
        self.leftsensor = ColorSensor(left)
        self.rightsensor = ColorSensor(right)
    def left(self):
        colour = self.leftsensor.color
        if colour == 0: # No colour found
            return "None"
        elif colour == 1: # Black
            return "Black"
        elif colour == 2: # Blue
            return "Blue"
        elif colour == 3: # Green
            return "Green"
        elif colour == 4: # Yellow
            return "Yellow"
        elif colour == 5: # Red
            return "Red"
        elif colour == 6: # White
            return "White"
        elif colour == 7: # Brown
            return "Brown"
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
            return "Black"
        elif colour == 2: # Blue
            return "Blue"
        elif colour == 3: # Green
            return "Green"
        elif colour == 4: # Yellow
            return "Yellow"
        elif colour == 5: # Red
            return "Red"
        elif colour == 6: # White
            return "White"
        elif colour == 7: # Brown
            return "Brown"
        else: # lmao this should never pass
            return "string lmao"
    def right_raw(self):
        colour = self.rightsensor.raw
        return colour    
    def cal(self):
        spkr = Sound()
        self.cal = {
            "green":{
                "r":[],
                "g":[],
                "b":[]
            },
            "white":{
                "r":[],
                "g":[],
                "b":[]
            },
            "black":{
                "r":[],
                "g":[],
                "b":[]
            }
        }
        spkr.speak("Place on green", play_type=Sound.PLAY_WAIT_FOR_COMPLETE)
        print("place on green")
        time.sleep(2)
        spkr.speak("Calibrating")
        print("starting green")
        for i in range(50):
            r = self.left_raw()
            self.cal["green"]["r"].append(r[0])
            self.cal["green"]["g"].append(r[1])
            self.cal["green"]["b"].append(r[2])
            r = self.right_raw()
            self.cal["green"]["r"].append(r[0])
            self.cal["green"]["g"].append(r[1])
            self.cal["green"]["b"].append(r[2])
            time.sleep(0.1)
        print("done")
        spkr.speak("Done", play_type=Sound.PLAY_WAIT_FOR_COMPLETE)
        
        time.sleep(5)
        print("place on white")
        spkr.speak("Place on white", play_type=Sound.PLAY_WAIT_FOR_COMPLETE)
        time.sleep(2)
        spkr.speak("Calibrating")
        print("starting white")
        for i in range(50):
            r = self.left_raw()
            self.cal["white"]["r"].append(r[0])
            self.cal["white"]["g"].append(r[1])
            self.cal["white"]["b"].append(r[2])
            r = self.right_raw()
            self.cal["white"]["r"].append(r[0])
            self.cal["white"]["g"].append(r[1])
            self.cal["white"]["b"].append(r[2])
            time.sleep(0.1)
        print("done")
        spkr.speak("Done", play_type=Sound.PLAY_WAIT_FOR_COMPLETE)

        print("place on black")
        spkr.speak("Place on black", play_type=Sound.PLAY_WAIT_FOR_COMPLETE)
        time.sleep(2)
        spkr.speak("Calibrating")
        print("starting")
        for i in range(50):
            r = self.left_raw()
            self.cal["black"]["r"].append(r[0])
            self.cal["black"]["g"].append(r[1])
            self.cal["black"]["b"].append(r[2])
            r = self.right_raw()
            self.cal["black"]["r"].append(r[0])
            self.cal["black"]["g"].append(r[1])
            self.cal["black"]["b"].append(r[2])
            time.sleep(0.1)
        print("done")
        spkr.speak("Done all", play_type=Sound.PLAY_WAIT_FOR_COMPLETE)
        json.dump(self.cal, open("/home/robot/cal.json", "w+"))

    def left2(self):
        raw = self.left_raw()

        if raw[0] in self.cal["black"]["r"] and raw[1] in self.cal["black"]["g"] and raw[2] in self.cal["black"]["b"]:
            return "Black"
        elif raw[0] in self.cal["green"]["r"] and raw[1] in self.cal["green"]["g"] and raw[2] in self.cal["green"]["b"]:
            return "Green"
        elif raw[0] in self.cal["white"]["r"] and raw[1] in self.cal["white"]["g"] and raw[2] in self.cal["white"]["b"]:
            return "White"
        else:
            return "None"
        
    def right2(self):
        raw = self.right_raw()

        if raw[0] in self.cal["black"]["r"] and raw[1] in self.cal["black"]["g"] and raw[2] in self.cal["black"]["b"]:
            return "Black"
        elif raw[0] in self.cal["green"]["r"] and raw[1] in self.cal["green"]["g"] and raw[2] in self.cal["green"]["b"]:
            return "Green"
        elif raw[0] in self.cal["white"]["r"] and raw[1] in self.cal["white"]["g"] and raw[2] in self.cal["white"]["b"]:
            return "White"
        else:
            return "None"
    
    def load_cal(self):
        self.cal = json.load(open("/home/robot/cal.json", "r"))

        
        
