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


log.info("Booted successfully!")
log.info("Starting engines, press CTRL+C to stop")

try:
    while True:
        while True:
            log.info("Engines Forward")
            try:
                engine.start()
                time.sleep(5)
            except KeyboardInterrupt: pass

            log.info("Engines Backward")
            try:
                engine.start(-100)
                time.sleep(5)
            except KeyboardInterrupt: pass

            log.info("Engines Left")
            try:
                engine.turn_left(50, 100)
                time.sleep(5)
            except KeyboardInterrupt: pass

            log.info("Engines Right")
            try:
                engine.turn_right(50, 100)
                time.sleep(5)
            except KeyboardInterrupt: pass

            log.info("Engines Hard Left") 
            try:
                engine.stop()
                engine.hard_left(100)
                time.sleep(5)
            except KeyboardInterrupt: pass

            log.info("Engines Hard Right")
            try:
                engine.stop()
                engine.hard_right(100)
                time.sleep(5)
            except KeyboardInterrupt: pass

except KeyboardInterrupt:
    log.debug("Detected CTRL+C, stopping robot")
    engine.stop()
    log.exit("Robot stopped, Goodbye!")
    sys.exit(0)