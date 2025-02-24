#! /usr/bin/python3

import log, sys
log.info("Linefollower Robot - STEM")


SOCK = False
if len(sys.argv) == 2:
    if "debug" in sys.argv :
        log.DEBUG = True
        log.debug("Debug mode enabled")
    elif "socket" in sys.argv:
        import socket
        log.info("Starting socket server on :8089")
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.bind(('localhost', 8089))
        serversocket.listen(1)
        log.info("Waiting for connection...")
        connection, address = serversocket.accept()
        log.done("Connected to "+str(address)+"! The dashboard is now available!")
        SOCK = True
        

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
    while True:
        data = {
            "left": sensors.left(),
            "right": sensors.right(),
            "leftengine": "100",
            "rightengine": "100",
            "mode": "linefollowing",
        }

        if sensors.left() == "black":
            engine.stop()
            engine.hard_left(25)
            data = {
                "left": sensors.left(),
                "right": sensors.right(),
                "leftengine": "50",
                "rightengine": "25",
                "mode": "linefollowing",
            }
            if SOCK:
                connection.send(json.dumps(data).encode())
            time.sleep(0.1)
            engine.start()
            data = {
                "left": sensors.left(),
                "right": sensors.right(),
                "leftengine": "100",
                "rightengine": "100",
                "mode": "linefollowing",
            }
        elif sensors.right() == "black":
            engine.stop()    
            engine.hard_right(25)
            data = {
                "left": sensors.left(),
                "right": sensors.right(),
                "leftengine": "25",
                "rightengine": "50",
                "mode": "linefollowing",
            }
            if SOCK:
                connection.send(json.dumps(data).encode())
            time.sleep(0.1)
            engine.start()
        elif sensors.left() == "green":
            # green dot
            log.info("Green dot detected")
            engine.stop()
            engine.turn_left(5)
            time.sleep(2)
            engine.stop()
            engine.start()
        if SOCK:
            connection.send(json.dumps(data).encode())

except KeyboardInterrupt:
    log.debug("Detected CTRL+C, stopping robot")
    engine.stop()
    log.exit("Robot stopped, Goodbye!")
    sys.exit(0)