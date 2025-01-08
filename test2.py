import time, datetime, keyboard, os
from timeclass import Time 

def cls():
     os.system('cls' if os.name=='nt' else 'clear')

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
        # time = (hour, minute, second, half_day)
        if half_day == "AM":
            if hour == 12:
                time = Time(0,minute,second, format)
            else:
                time = Time(hour, minute, second, format)
        else:
            if hour == 12:
                time = Time(hour, minute, second, format)
            else:
                time = Time(hour+12, minute, second, format)
        
    else:
        # time = (hour, minute, second)
        time = Time(hour, minute, second)
        
    return time

def choose_format():
    format_choice = input("Choose the time format (12h/24h): ")
    if format_choice != "12h" and format_choice != "24h":
        return choose_format()
    else:
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

    if alarm and current_time[0] * 3600 + current_time[1] * 60 + current_time[2] <= alarm[0] * 3600 + alarm[1] * 60 + alarm[2] + max_display:
        cls()

def display_alarm(clock, alarm, max_display):
    if alarm and clock[0] * 3600 + clock[1] * 60 + clock[2] >= alarm[0] * 3600 + alarm[1] * 60 + alarm[2] and clock[0] * 3600 + clock[1] * 60 + clock[2] <= alarm[0] * 3600 + alarm[1] * 60 + alarm[2] + max_display:
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
    # alarm = choose_alarm(format) # value: (h,m,s)
    clock = set_time(format) # value: (h,m,s)

    
    cls()
    while True :
        
        time.sleep(1.0)
        #clock = datetime.datetime.now()
        clock.increment_time()
        print("\r" + f"{clock}", end="")

        #current_time = (clock.strftime('%H'), clock.strftime('%M'), clock.strftime('%S'))
        # message = display_alarm(clock, alarm, max_display)
        # display_time(clock, max_display, alarm, message)
        
        
        #TODO need to not actualize clock variable when paused
        try:
            if keyboard.is_pressed('a'):
                keyboard.wait('b')
        except:
            print("error")
        
        
main()
