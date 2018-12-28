import inputs
import anki_vector
from inputs import get_gamepad
from anki_vector.util import degrees, distance_mm, speed_mmps
import time
import utils
import asyncio

async def main():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial) as robot:
        utils.pprint("Starting manual control", robot)
        robot.behavior.drive_off_charger()
        while True:
            for event in get_gamepad():
                if event.code == "BTN_SOUTH" and event.state == 1: # A Button
                    print("[inputs]", event.ev_type, event.code, event.state)
                    utils.smack(robot)
                if event.code == "ABS_HAT0Y" and event.state == -1: # DPAD UP
                    print("[inputs]", event.ev_type, event.code, event.state)
                    utils.lift("UP", robot)
                elif event.code == "ABS_HAT0Y" and event.state == 1: # DPAD DOWN
                    print("[inputs]", event.ev_type, event.code, event.state)
                    utils.lift("DOWN", robot)
                if event.code == "BTN_TR" and event.state == 1: # Right Button
                    print("[inputs]", event.ev_type, event.code, event.state)
                    print("FINDING CHARGER\n")
                    utils.pprint("FINDING CHARGER", robot)
                    robot.behavior.drive_on_charger()
                if event.code == "ABS_Y" and event.state >= 3000: # Drive forward
                    print("[inputs]", event.ev_type, event.code, event.state)
                    print("DRIVING STRAIGHT\n")
                    robot.behavior.drive_straight(distance_mm(200), speed_mmps(150))
                elif event.code == "ABS_Y" and event.state <= -3000: # Drive backwards
                    print("[inputs]", event.ev_type, event.code, event.state)
                    print("DRIVING BACK\n")
                    robot.behavior.drive_straight(distance_mm(-200), speed_mmps(150))
                if event.code == "ABS_RX" and event.state >= 3000: # Turn Right
                    robot.behavior.turn_in_place(degrees(-45))
                    print("[inputs]", event.ev_type, event.code, event.state)
                    print("TURNING 90 DEGREES\n")
                elif event.code == "ABS_RX" and event.state <= -3000: # Turn Left
                    robot.behavior.turn_in_place(degrees(45))
                    print("[inputs]", event.ev_type, event.code, event.state)
                    print("TURNING -90 DEGREES\n")

if __name__ == "__main__":
    asyncio.run(main())
