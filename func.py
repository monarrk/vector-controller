import anki_vector
from anki_vector.util import degrees, distance_mm, speed_mmps
from anki_vector.behavior import MIN_HEAD_ANGLE, MAX_HEAD_ANGLE
from anki_vector.util import degrees

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

def move_head(robot):
    hangl = robot.head_angle_rad
    if hangl <= 0.5:
        robot.behavior.set_head_angle(MAX_HEAD_ANGLE)
    else:
        robot.behavior.set_head_angle(MIN_HEAD_ANGLE)
