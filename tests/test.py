from robot import *
engine = Engine(motor.OUTPUT_A, motor.OUTPUT_D)

engine.start()
try: 
    while True: pass
except KeyboardInterrupt:
    engine.stop()
engine.start(-100)
try: 
    while True: pass
except KeyboardInterrupt:
    engine.stop()
engine.turn_left()
try: 
    while True: pass
except KeyboardInterrupt:
    engine.stop()
engine.turn_right()
try: 
    while True: pass
except KeyboardInterrupt:
    engine.stop()
    print("goodbye!")