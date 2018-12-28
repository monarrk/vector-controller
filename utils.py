import anki_vector
from anki_vector.util import degrees, distance_mm, speed_mmps

def smack(robot):
    print("SMASHING\n")
    robot.behavior.set_lift_height(1, 0, 0, 0, 0)
    robot.behavior.set_lift_height(0, 0, 0, 0, 0)

def lift(dire, robot):
    print(f"MOVING LIFT {dire}\n")
    if dire == "UP":
        robot.behavior.set_lift_height(1, 0, 0, 0, 0)
    elif dire == "DOWN":
        robot.behavior.set_lift_height(0, 0, 0, 0, 0)
    else:
        print(f"[lift] ERR, {dire} IS NOT A VALID DIRECTION\n\n")

def pprint(msg, robot):
    robot.say_text(msg)