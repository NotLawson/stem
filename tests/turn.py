import robot
import time
engine = robot.Engine(robot.motor.OUTPUT_A, robot.motor.OUTPUT_B)

while True:
    input()
    engine.hard_left(30)
    time.sleep(1.12)
    engine.stop()
