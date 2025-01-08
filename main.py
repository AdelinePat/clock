import time, datetime, keyboard, os

def cls():
     os.system('cls' if os.name=='nt' else 'clear')

def clock_ticking(clock):
    
    if len(clock) == 4:
        if clock[2] < 59:
            clock = (clock[0], clock[1], clock[2]+1, clock[3])
        else:
            clock = (clock[0], clock[1], 0, clock[3])
            if clock[1] < 59:
                clock = (clock[0], clock[1]+1, clock[2], clock[3])
            else:
                clock = (clock[0], 0, clock[2], clock[3])
                if clock[0] < 13:
                    clock = (clock[0]+1, clock[1], clock[2], clock[3])
                
                if clock[0] == 12 and clock[1] == 0 and clock[2] == 0:
                    if clock[3] == "AM":
                        clock = (clock[0], clock[1], clock[2], "PM")
                    else:
                        clock = (clock[0], clock[1], clock[2], "AM")

                if clock[0] == 13:
                    clock = (1, clock[1], clock[2], clock[3]) 

    else:
        if clock[2] < 59:
            clock = (clock[0], clock[1], clock[2]+1)
        else:
            clock = (clock[0], clock[1], 0)
            if clock[1] < 59:
                clock = (clock[0], clock[1]+1, clock[2])
            else:
                clock = (clock[0], 0, clock[2]) 
                if clock[0] < 23:
                    clock = (clock[0]+1, clock[1], clock[2]) 
                else:
                    clock = (0, clock[1], clock[2]) 
    
    return clock

def set_time(format):
    min_hour = 0
    max_hour = 23
    hour = -1
    minute = -1
    second = -1

    if format == "12h":
        half_day = ""
        while half_day != "AM" and half_day != "PM":
            half_day = input("AM or PM? ").upper().strip()
        min_hour = 1
        max_hour = 12
    
    while hour < min_hour or hour > max_hour:
        hour = int(input(f"Enter hours ({min_hour}-{max_hour}): "))
        if hour < 0 or hour > max_hour:
            print(f"Please enter a number between {min_hour} and {max_hour}!")

    while minute < 0 or minute > 59:
        minute = int(input("Enter minutes (0-59): "))
        if minute < 0 or minute > 59:
            print("Please enter a number between 0 and 59!")

    while second < 0 or second > 59:
        second = int(input("Enter seconds (0-59): "))
        if second < 0 or second > 59:
            print("Please enter a number between 0 and 59!")

    if format == "12h":
        time = (hour, minute, second, half_day)
    else:
        time = (hour, minute, second)

    return time

def choose_format():
    """ Ask the user to choose between 12h or 24h format """
    format_choice = input("Choose the time format (12h/24h): ")
    if format_choice != "12h" and format_choice != "24h":
        return choose_format()
    return format_choice

def choose_alarm(format):
    alarm_choice = input("Do you want to set an alarm ?(yes/no):").lower().strip()
    if alarm_choice != "yes" and alarm_choice != "y" and alarm_choice != "no" and alarm_choice != "n":
        return choose_alarm(format)
    elif alarm_choice == "yes" or alarm_choice == "y":
        alarm_clock = set_time(format)  
        return alarm_clock
    else:
        return None

def format_time(time):
    if len(str(time[0])) == 1:
        temp_str = "0" + str(time[0]) + ":"
    else:
        temp_str = str(time[0]) + ":"

    if len(str(time[1])) == 1:
        temp_str += "0" + str(time[1]) + ":"
    else:
        temp_str += str(time[1]) + ":"

    if len(str(time[2])) == 1:
        temp_str += "0" + str(time[2])
    else:
        temp_str += str(time[2])

    if len(time) == 4:
        temp_str += " " + time[3]
    
    return temp_str

# update time in terminal
def display_time(current_time, max_display, alarm, message=""):
    current_time_str = format_time(current_time)
   
    #current_time_str = str(current_time[0]) + ":" + str(current_time[1]) + ":" + str(current_time[2]) + " "
    if alarm:
        #alarm_str = "alarm : " + str(alarm[0]) + ":" + str(alarm[1]) + ":" + str(alarm[2]) + " " 
        alarm_str = " ; alarm : " + format_time(alarm)
    else:
        alarm_str = ""

    print("\r" + current_time_str + alarm_str + message + " ", end="")

    if alarm and current_time[0] * 3600 + current_time[1] * 60 + current_time[2] <= alarm[0] * 3600 + alarm[1] * 60 + alarm[2] + max_display:
        cls()
        print("\r" + current_time_str + alarm_str + message + " ", end="")

def display_alarm(clock, alarm, max_display):
    
    if alarm and len(clock) == 4 and clock[3] != alarm[3]:
        if clock[3] == "AM":
            if alarm and clock[0] * 3600 + clock[1] * 60 + clock[2] >= (alarm[0]+12) * 3600 + alarm[1] * 60 + alarm[2] and clock[0] * 3600 + clock[1] * 60 + clock[2] <= (alarm[0]+12) * 3600 + alarm[1] * 60 + alarm[2] + max_display:
                ring = "Ring ring! Ring ring!"
                message = (f"{ring:>30}")
                return message
            else:
                message = ""
                return message
        else:
            if alarm and (clock[0]+12) * 3600 + clock[1] * 60 + clock[2] >= alarm[0] * 3600 + alarm[1] * 60 + alarm[2] and (clock[0]+12) * 3600 + clock[1] * 60 + clock[2] <= alarm[0] * 3600 + alarm[1] * 60 + alarm[2] + max_display:
                ring = "Ring ring! Ring ring!"
                message = (f"{ring:>30}")
                return message
            else:
                message = ""
                return message
    else:
        if alarm and clock[0] * 3600 + clock[1] * 60 + clock[2] >= alarm[0] * 3600 + alarm[1] * 60 + alarm[2] and clock[0] * 3600 + clock[1] * 60 + clock[2] <= alarm[0] * 3600 + alarm[1] * 60 + alarm[2] + max_display:
            ring = "Ring ring! Ring ring!"
            message = (f"{ring:>30}")
            return message
        else:
            message = ""
            return message
        
def main():
    max_display = 10 #10 seconds

    format = choose_format() # value : "12h" / "24h"
    alarm = choose_alarm(format) # value: (h,m,s)
    clock = set_time(format) # value: (h,m,s)
    
    cls()
    while True :

        #clock = datetime.datetime.now()
        clock = clock_ticking(clock)

        #current_time = (clock.strftime('%H'), clock.strftime('%M'), clock.strftime('%S'))
        message = display_alarm(clock, alarm, max_display)
        display_time(clock, max_display, alarm, message)
        
        for i in range(5):
            time.sleep(0.2)
            try:
                if keyboard.is_pressed('space'):
                    keyboard.wait('space')
            except:
                print("error")

        #TODO need to not actualize clock variable when paused
        
main()