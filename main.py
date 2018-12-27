import inputs
import anki_vector
from inputs import get_gamepad
from anki_vector.util import degrees, distance_mm, speed_mmps
import time

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




def main():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        robot.behavior.drive_off_charger()
        while True:
            for event in get_gamepad():
                print("[inputs]", event.ev_type, event.code, event.state)
                if event.code == "BTN_SOUTH" and event.state == 1:
                    smack(robot)
                if event.code == "ABS_HAT0Y" and event.state == -1:
                    lift("UP", robot)
                elif event.code == "ABS_HAT0Y" and event.state == 1:
                    lift("DOWN", robot)

if __name__ == "__main__":
    main()