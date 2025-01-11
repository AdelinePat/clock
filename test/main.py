import time, threading
import alarm, display
from Clockclass import Clock


def command_terminal(event, clock_time):
    while True:
        command = display.input_command()
        match command:
            case "mode":
                clock_time.mode = not clock_time.mode
                # if clock_time.format == "AM":
                #    clock_time.clock = (clock_time.clock[0]+12, clock_time.clock[1], clock_time.clock[2])
                #    clock_time.format = "PM"
                # else:
                #    clock_time.clock = (clock_time.clock[0]-12, clock_time.clock[1], clock_time.clock[2])
                #    clock_time.format = "AM"
                continue
            case "clock":
                event.clear()
                clock_time.clock = clock_time.change_clock()
                event.set()
                continue
            case "alarm":
                pass
            case "stop":
                event.clear()
                display.message_stop()
            case "start":
                event.set()
                display.message_start()
            case _:
                continue

def main():
    clock_time = Clock((0,0,0),0,"", False)
    event = threading.Event()

    display.all_clear()

    #display.message_first_time()

    clock_time.change_clock()

    #TODO First time configuration
    threading.Thread(target=command_terminal, args=(event, clock_time)).start()
    event.set()

    threading.Thread(target=clock_time.display_clock, args=(event)).start()
    #if alarm
    #   threading.Thread(target=alarm.display_alarm).start()

main()