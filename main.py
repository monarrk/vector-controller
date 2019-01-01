import inputs
import anki_vector
from inputs import get_gamepad
from anki_vector.util import degrees, distance_mm, speed_mmps
import time
import func
import asyncio
from colorama import Fore, Back, Style, init

async def main():
    args = anki_vector.util.parse_command_args()
    loop = True
    with anki_vector.Robot(args.serial) as robot:
        func.pprint("Starting manual control", robot)
        robot.behavior.drive_off_charger()
        print(Fore.GREEN + "BEGINNING LOOP STAGE\n-----------------------------------\n\n")
        print(Style.RESET_ALL)
        while loop == True:
            for event in get_gamepad():
                if event.code == "BTN_SOUTH" and event.state == 1: # A Button
                    print("[inputs]", event.ev_type, event.code, event.state)
                    func.smack(robot)

                if event.code == "ABS_HAT0Y": # DPAD
                    print("[inputs]", event.ev_type, event.code, event.state)
                    if event.state == -1: # UP
                        func.lift("UP", robot)
                    elif event.state == 1: # DOWN
                        func.lift("DOWN", robot)

                if event.code == "BTN_TR" and event.state == 1: # Right Button
                    print("[inputs]", event.ev_type, event.code, event.state)
                    print("FINDING CHARGER\n")
                    func.pprint("FINDING CHARGER", robot)
                    robot.behavior.drive_on_charger()

                if event.code == "BTN_EAST" and event.state == 1: # B Button
                    print("[inputs]", event.ev_type, event.code, event.state)
                    print("MOVING HEAD\n")
                    func.move_head(robot)

                if event.code == "ABS_Y" and event.state >= 3000: # Drive forward
                    print("[inputs]", event.ev_type, event.code, event.state)
                    print("DRIVING STRAIGHT\n")
                    robot.behavior.drive_straight(distance_mm(300), speed_mmps(200))
                elif event.code == "ABS_Y" and event.state <= -3000: # Drive backwards
                    print("[inputs]", event.ev_type, event.code, event.state)
                    print("DRIVING BACK\n")
                    robot.behavior.drive_straight(distance_mm(-300), speed_mmps(150))

                if event.code == "ABS_RX" and event.state >= 3000: # Turn Right
                    robot.behavior.turn_in_place(degrees(-45))
                    print("[inputs]", event.ev_type, event.code, event.state)
                    print("TURNING 90 DEGREES\n")
                elif event.code == "ABS_RX" and event.state <= -3000: # Turn Left
                    robot.behavior.turn_in_place(degrees(45))
                    print("[inputs]", event.ev_type, event.code, event.state)
                    print("TURNING -90 DEGREES\n")

                if event.code == "BTN_START" and event.state == 1: # Kill cmd
                    print("[inputs]", event.code, event.state)
                    print(Fore.RED + "KILLING LOOP, BYEBYE!!")
                    loop = False

if __name__ == "__main__":
    init()
    asyncio.run(main())
