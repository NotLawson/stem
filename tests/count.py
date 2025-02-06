import robot
import time
engine = robot.Engine(robot.motor.OUTPUT_A, robot.motor.OUTPUT_B)

start = time.perf_counter()

engine.hard_left(30)
print("go")
try:
    while True: pass
except KeyboardInterrupt:
    end = time.perf_counter()
    engine.stop()

total = end-start

print("Took",total)