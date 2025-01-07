import time, datetime, keyboard, os
def cls():
     os.system('cls' if os.name=='nt' else 'clear')

def clock_ticking(clock):
    
    if len(clock) == 4:
        clock = (clock[0], clock[1], clock[2]+1, clock[3])

        if clock[2] == 60:
            clock = (clock[0], clock[1]+1, 0, clock[3])  

        if clock[1] == 60:
            clock = (clock[0]+1, 0, clock[2], clock[3]) 

        if clock[0] == 12 and clock[1] == 0 and clock[2] == 0:
            if clock[3] == "AM":
                clock = (clock[0], clock[1], clock[2], "PM")
            else:
                clock = (clock[0], clock[1], clock[2], "AM")

        if clock[0] == 13:
            clock = (0, clock[1], clock[2], clock[3]) 

    else:
        clock = (clock[0], clock[1], clock[2]+1)

        if clock[2] == 60:
            clock = (clock[0], clock[1]+1, 0)  

        if clock[1] == 60:
            clock = (clock[0]+1, 0, clock[2]) 

        if clock[0] == 24:
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
        hour = int(input(f"Enter hours (0-{max_hour}): "))
        if hour < 0 or hour > max_hour:
            print(f"Please enter a number between 0 and {max_hour}!")

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
    format_choice = ""
    while format_choice != "12h" and format_choice != "24h":
        format_choice = input("Choose the time format (12h/24h): ")
        if format_choice != "12h" and format_choice != "24h":
            print("Enter 12h or 24h to continue!")
    return format_choice

def choose_alarm(format):
    alarm_choice = ""
    while alarm_choice != "yes" and alarm_choice != "y" and alarm_choice != "no" and alarm_choice != "n":
        alarm_choice = input("Do you want to set an alarm ?(yes/no):").lower().strip()
        if alarm_choice == "yes" or alarm_choice == "y":
            alarm_clock = set_time(format)
        else:
            alarm_clock = None    
    return alarm_clock

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
    if alarm and int(current_time[2]) == int(alarm[2]) + max_display:
        cls()

def display_alarm(clock, alarm, max_display):
    if alarm and clock >= alarm and int(clock[2]) < int(alarm[2])+max_display:
        ring = "Ring ring! Ring ring!"
        message = (f"{ring:>30}")
        # Blinking message
        #while clock[1] < alarm_time[1] + 1:
            #if clock[2] % 2 == 0:
                #return "Ring ring! Ring ring!"
            #else:
                #return ""   
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
        
        time.sleep(1.0)
        #clock = datetime.datetime.now()
        clock = clock_ticking(clock)

        #current_time = (clock.strftime('%H'), clock.strftime('%M'), clock.strftime('%S'))
        message = display_alarm(clock, alarm, max_display)
        display_time(clock, max_display, alarm, message)
        
        
        #TODO need to not actualize clock variable when paused
        try:
            if keyboard.is_pressed('a'):
                keyboard.wait('b')
        except:
            print("error")
        
        
main()
