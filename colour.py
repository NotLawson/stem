import log, sys, time
from robot import *
log.info("init sensors...")
sensors = LineFollowerSensors(sensor.INPUT_1, sensor.INPUT_4)
log.info("init sensors done")

while True:
    try:
        sys.stdout.write("L: "+str(sensors.left_reflect())+"   R: "+str(sensors.right_reflect())+"                 \r")
        time.sleep(0.1)
    except KeyboardInterrupt:
        break