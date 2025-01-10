import time, threading
import alarm, clock, message
from Clockclass import Clock

clock_time = Clock((0,0,0),0,"", False)
event = threading.Event()

#TODO variable for each line (l) + the "clear line" separated + the "save cursor"
# ANSI codes
dic_cursor = {
    "delete_line_1-clock": "\033[s\033[H\033[2K",
    "delete_line_2-alarm": "\033[s\033[H\033[1B\033[2K",
    "delete_line_3-message": "\033[H\033[2B\033[2K",
    "delete_line_4-command": "\033[H\033[3B\033[2K",
    "delete_line_5-info": "\033[H\033[4B\033[2K",
    "delete_line_6-error": "\033[H\033[5B\033[2K",

    "cursor_position_start": "\033[H",
    "cursor_position_load": "\033[u",
    "delete_line": "\033[2K",
    "delete_all_after_position": "\033[0J",
    "delete_all": "\033[H\033[0J"
}

def command_terminal(event, clock_time):
    while True:
        command = input(f"{dic_cursor["delete_line_4-command"]}{dic_cursor["delete_all_after_position"]}Commande : ")
        match command:
            case "mode":
                print(f"{dic_cursor["delete_line_3-message"]}{clock_time.clock}")
                clock_time.mode = not clock_time.mode
                if clock_time.format == "AM":
                    clock_time.clock = (clock_time.clock[0]+12, clock_time.clock[1], clock_time.clock[2])
                    clock_time.format = "PM"
                else:
                    clock_time.clock = (clock_time.clock[0]-12, clock_time.clock[1], clock_time.clock[2])
                    clock_time.format = "AM"
                continue
            case "clock":
                event.clear()
                clock_time.clock = clock.change_clock(dic_cursor, clock_time)
                event.set()
                continue
            case "stop":
                event.clear()
                message.stop(dic_cursor)
            case "start":
                event.set()
                message.start(dic_cursor)
            case _:
                continue

def main():
    print(dic_cursor["delete_all"], end="")
    threading.Thread(target=command_terminal, args=(event, clock_time)).start()
    event.set()
    threading.Thread(target=clock.display_clock, args=(event, clock_time, dic_cursor)).start()
    #threading.Thread(target=alarm.display_alarm).start()

main()