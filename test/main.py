import threading, time
import display
from Clock_class import Clock
from Alarm_class import Alarm

def command_terminal(event, clock_time):
    while True:
        display.message_help()
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
            case "horloge":
                event.clear()
                clock_time.clock = clock_time.change_clock()
                event.set()
                continue
            case "alarme":
                if not alarm_time:
                    alarm_time = Alarm((0,0,0),0,"", clock_time.mode)
                    threading.Thread(target=alarm_time.display_alarm).start()
                alarm_time.alarm = alarm_time.change_alarm()
                continue
            case "stop":
                event.clear()
                display.message_stop()
                continue
            case "demarrer":
                event.set()
                display.message_start()
                continue
            case "aide":
                display.message_help()
                continue
            case "quitter":
                display.message_byebye()
                time.sleep(3)
                break
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

main()