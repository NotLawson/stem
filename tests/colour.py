from robot import *
import sys, time

print("init sensors...")
sensors = Sensors(sensor.INPUT_1, sensor.INPUT_4)
us = UltrasonicSensor(sensor.INPUT_3)
print("init sensors done")

while True:
    try:
        sys.stdout.write("L: "+sensors.left()+"   R: "+sensors.right()+" D: "+str(round(us.distance_centimeters, 1))+"                 \r")
        time.sleep(0.1)
    except KeyboardInterrupt:
        break