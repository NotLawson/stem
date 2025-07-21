#! /usr/bin/python3

import log,sys,time
log.info("Linefollower Robot - STEM")

if len(sys.argv) > 1:
    if sys.argv[1] == "debug":
        log.DEBUG = True
        log.info("Debug mode enabled")
    else:
        log.error("Invalid argument: "+sys.argv[1])
        sys.exit(1)

log.debug("Loading Robot...")
from robot import *

log.debug("Initiating Engine...")
try: engine = Engine(motor.OUTPUT_D, motor.OUTPUT_A)
except Exception as e: 
    log.error("Failed to initiate engine: "+str(e))
    sys.exit(1)
log.debug("Engine initiated")

log.debug("Initiating Sensors...")
try: sensors = LineFollowerSensors(sensor.INPUT_4, sensor.INPUT_1)
except Exception as e: 
    log.error("Failed to initiate sensors: "+str(e))
    sys.exit(1)
log.debug("Sensors initiated")

log.info("Booted successfully!")
log.info("Starting Linefollower, press CTRL+C to stop")

try:
    engine.start()
    starttime = time.time()
    while True:
        left = sensors.left()
        right = sensors.right()
        if not log.DEBUG:
            sys.stdout.write("L: "+str(left)+"   R: "+str(right)+"     Time: "+str(int(time.time()-starttime))+"          \r")
        sys.stdout.flush()
        if (left == "green" and right == "green"):
            engine.stop()
            # finished
            log.info("Finished line, stopping")
            break
        elif left == "black":
            engine.stop()
            engine.hard_left(25)
            time.sleep(0.1)
            engine.start()
        elif right == "black":
            engine.stop()
            engine.hard_right(25)
            time.sleep(0.1)
            engine.start()
        elif left == "green":
            # green dot
            engine.stop()
            engine.turn_left(5)
            time.sleep(1)
            engine.stop()
            engine.start()
        
        log.info("Moved on to searching for spill victim")
        # Okay, I was watching some videos of other robots in this challenge and saw this idea used
        # When the robot detects the spill area, it will move out of conventional line following and search for the entrance to
        # reorient itself before continueing to search for the victim.
        # I'll work on a similar system, I reckon it's a good idea.
        
except KeyboardInterrupt:
    log.debug("Detected CTRL+C, stopping robot")
    engine.stop()

total = time.time() - starttime
log.info("Total time: "+str(total)+" seconds")
log.exit("Robot stopped, Goodbye!")
sys.exit(0)
