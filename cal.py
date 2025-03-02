import log, time, pickle
from robot import *
log.info("init sensors...")
sensors = LineFollowerSensors(sensor.INPUT_1, sensor.INPUT_4)
log.info("init sensors done")

log.info("Start calibration")
cmd = log.ask("Record or load? [r/l] ")
if cmd == "l":
    log.info("Loading...")
    with open("colours.pickle", "rb") as f:
        data = pickle.load(f)
    white = data["white"]
    black = data["black"]
    green = data["green"]
    log.done("Loaded")
    
    white_vals = {
        "r": [],
        "g": [],
        "b": [],
    }
    for colour in white:
        white_vals["r"].append(colour[0])
        white_vals["g"].append(colour[1])
        white_vals["b"].append(colour[2])

    white = {
        "max": [max(white_vals["r"]), max(white_vals["g"]), max(white_vals["b"])],
        "min": [min(white_vals["r"]), min(white_vals["g"]), min(white_vals["b"])],
        "avg": [sum(white_vals["r"])/len(white_vals["r"]), sum(white_vals["g"])/len(white_vals["g"]), sum(white_vals["b"])/len(white_vals["b"])],
    }

    log.info("White data: "+str(white))

    black_vals = {
        "r": [],
        "g": [],
        "b": [],
    }
    for colour in black:
        black_vals["r"].append(colour[0])
        black_vals["g"].append(colour[1])
        black_vals["b"].append(colour[2])

    black = {
        "max": [max(black_vals["r"]), max(white_vals["g"]), max(white_vals["b"])],
        "min": [min(black_vals["r"]), min(white_vals["g"]), min(white_vals["b"])],
        "avg": [sum(black_vals["r"])/len(black_vals["r"]), sum(black_vals["g"])/len(black_vals["g"]), sum(black_vals["b"])/len(black_vals["b"])],
    }

    log.info("Black data:"+str(black))

    green_vals = {
        "r": [],
        "g": [],
        "b": [],
    }
    for colour in green:
        green_vals["r"].append(colour[0])
        green_vals["g"].append(colour[1])
        green_vals["b"].append(colour[2])

    green = {
        "max": [max(green_vals["r"]), max(green_vals["g"]), max(green_vals["b"])],
        "min": [min(green_vals["r"]), min(green_vals["g"]), min(green_vals["b"])],
        "avg": [sum(green_vals["r"])/len(green_vals["r"]), sum(green_vals["g"])/len(green_vals["g"]), sum(green_vals["b"])/len(green_vals["b"])],
    }

    log.info("Green data:"+str(green))

elif cmd == "r":
    log.info("Recording...")

    log.warn("WHITE")
    time.sleep(2)
    log.info("3")
    time.sleep(1)
    log.info("2")
    time.sleep(1)
    log.info("1")
    time.sleep(1)
    log.info("Recording")
    white = []
    for i in range(50):
        white.append(sensors.left_raw())
        white.append(sensors.right_raw())
        time.sleep(0.1)
    log.info("WHITE done")

    log.warn("BLACK")
    time.sleep(2)
    log.info("3")
    time.sleep(1)
    log.info("2")
    time.sleep(1)
    log.info("1")
    time.sleep(1)
    log.info("Recording")
    black = []
    for i in range(50):
        black.append(sensors.left_raw())
        black.append(sensors.right_raw())
        time.sleep(0.1)
    log.info("BLACK done")

    log.warn("GREEN")
    time.sleep(2)
    log.info("3")
    time.sleep(1)
    log.info("2")
    time.sleep(1)
    log.info("1")
    time.sleep(1)
    log.info("Recording")
    green = []
    for i in range(50):
        green.append(sensors.left_raw())
        green.append(sensors.right_raw())
        time.sleep(0.1)
    log.info("GREEN done")

    log.info("Saving...")
    data = {
        "white": white,
        "black": black,
        "green": green,
    }
    with open("colours.pickle", "wb") as f:
        pickle.dump(data, f)
    log.done("Saved")
    log.done("Calibration done!")

log.exit("Exiting")