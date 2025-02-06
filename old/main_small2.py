#! /usr/bin/python3

## Search and Rescue for robocup ##
from robot import *
from ev3dev2.sound import Sound
import sys
import time
from term import term

pings = 0
last = 0.0

s = Engine.SPEED/2

def ping():
    global pings, last, engine
    now = time.perf_counter()
    t = now-last
    if t <= 1: 
        pings += 1
        print("Ping:", pings)
        if pings>=10:
            print("push")
            engine.start(30)
            time.sleep(0.2)
            engine.stop()
    else: pings = 0

def dodge():
    engine.hard_left(30)
    time.sleep(0.56)
    engine.stop()
    engine.start(s)
    time.sleep(1.7)
    engine.stop()
    engine.hard_right(30)
    time.sleep(0.56)
    engine.stop()
    engine.start(s)
    time.sleep(3)
    engine.stop()
    engine.hard_right(30)
    time.sleep(0.56)
    engine.stop()
    engine.start(s)
    time.sleep(1.5)
    engine.stop()
    engine.hard_left(30)
    time.sleep(0.56)
    engine.stop()
    engine.start()
    
print("init engine...")
engine = Engine(motor.OUTPUT_B, motor.OUTPUT_A)
pincer = motor.MediumMotor(motor.OUTPUT_C)
print("init engine  done  ")
print("init sensors...")
sensors = Sensors(sensor.INPUT_1, sensor.INPUT_4)
sonar = UltrasonicSensor(sensor.INPUT_3)
frontsonar = UltrasonicSensor(sensor.INPUT_2)
print("init sensors  done")

sound = Sound()

sound.play_file("/home/robot/beep.wav", play_type=Sound.PLAY_NO_WAIT_FOR_COMPLETE)
time.sleep(2.8)

left = " "
right = " "

#input("Waiting for input...\n")
engine.start()
while True:
    try:
        term(left, right)
        if frontsonar.distance_centimeters <= 4:
            dodge()
        elif sensors.left()=="Green" and sensors.right()=="Green":
            engine.stop()
            term("G", "G")
            print("\nSearching...")
            break
        elif sensors.left()=="Black":
            ping()
            left = "B"
            term(left, right)
            engine.stop()
            while sensors.left()=="Black":
                engine.hard_left(30)
                time.sleep(0.1)
            engine.stop()
            engine.start(s)
        elif sensors.right()=="Black":
            ping()
            right = "B"
            term(left, right)
            engine.stop()
            while sensors.right()=="Black":
                engine.hard_right(30)
                time.sleep(0.1)
            engine.stop()
            engine.start(s)
        elif sensors.right()=="Green":
            right = "G"
            term(left, right)
            time.sleep(0.3)
            engine.hard_right(20)
            time.sleep(0.5)
            engine.stop()
            engine.start(s)
            time.sleep(0.3)
        elif sensors.left()=="Green":
            left = "G"
            term(left, right)
            time.sleep(0.3)
            engine.hard_left(20)
            time.sleep(0.5)
            engine.stop()
            engine.start(s)
            time.sleep(0.3)
        left = " "
        right = " "
    except KeyboardInterrupt:
        break

## Search
print("This is where the robot finds the can")
engine.start()
time.sleep(2)
engine.stop()

engine.hard_left(30)
time.sleep(0.56)
engine.stop()
engine.hard_left(5)

starttime = time.perf_counter()
while True:
    dist = sonar.distance_centimeters
    sys.stdout.write("D: "+str(round(dist, 1))+"              \r")
    time.sleep(0.01)
    if dist < 50:
        break
endtime = time.perf_counter() - starttime
print("seen can, adjusting")
time.sleep(0.7)
print("killing engine")
engine.stop()
print("opening pincers")
pincer.on(10)
time.sleep(0.3) # set time
pincer.off()
print("finding can")
engine.start(-10)
while True:
    dist = sonar.distance_centimeters
    sys.stdout.write("D: "+str(round(dist, 1))+"              \r")
    time.sleep(0.01)
    if dist < 8:
        break
print("closing arms")
pincer.on(-10)
time.sleep(0.5) # set time
pincer.off()
print("charging!")
engine.start(-100)
try:
    time.sleep(1)
except KeyboardInterrupt:
    pass
engine.stop()
print("reverse")

print("let go")
pincer.on(10)
time.sleep(0.3) # set time
pincer.off()

print("move back")
engine.start(100)
time.sleep(1)
engine.stop()

print("spin back")
engine.hard_right(5)
time.sleep(endtime)
engine.stop()

print("spin back to face the track")
engine.hard_right(30)
time.sleep(0.56)
engine.stop()

engine.start(-engine.SPEED)
time.sleep(3)
engine.stop()



engine.start()
while True:
    try:
        if sensors.left()=="Black":
            left = "B"
            term(left, right)
            engine.stop()
            while sensors.left()=="Black":
                engine.hard_left(30)
                time.sleep(0.2)
            engine.stop()
            engine.start()
        elif sensors.right()=="Black":
            right = "B"
            term(left, right)
            engine.stop()
            while sensors.right()=="Black":
                engine.hard_right(30)
                time.sleep(0.2)
            engine.stop()
            engine.start()
        left = " "
        right = " "
    except KeyboardInterrupt:
        break

engine.stop()

print("thank the stars thing thing works")