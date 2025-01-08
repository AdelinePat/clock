import time, datetime, keyboard, os
from timeclass import Time
from timeclass import Alarm 

def cls():
     os.system('cls' if os.name=='nt' else 'clear')

def set_time(format):
    min_hour = 0
    max_hour = 23
    hour = -1
    minute = -1
    second = -1

    if format == "12h":
        half_day = input("AM or PM? ").upper().strip()
        if half_day != "AM" and half_day != "PM":
            return set_time(format)      
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
                time = Time(0, minute,second, format)
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
    format_choice = input("Choose the time format (12h/24h): ").lower().strip()
    if format_choice != "12h" and format_choice != "24h":
        return choose_format()
    else:
        return format_choice

def choose_alarm(format):
    alarm_choice = input("Do you want to set an alarm ?(yes/no):").lower().strip()
    if alarm_choice != "yes" and alarm_choice != "y" and alarm_choice != "no" and alarm_choice != "n":
        return choose_alarm()
    elif alarm_choice == "yes" or alarm_choice == "y":
        alarm = set_time(format)
        alarm_clock = Alarm(alarm.hour, alarm.minute, alarm.second, format, True)
    else:
        alarm_clock = Alarm(0, 0, 0, "24h", False)
    return alarm_clock


# def display_alarm(clock, alarm, max_display):
#      if alarm and clock.in_seconds() >= alarm[0] * 3600 + alarm[1] * 60 + alarm[2] and clock[0] * 3600 + clock[1] * 60 + clock[2] <= alarm[0] * 3600 + alarm[1] * 60 + alarm[2] + max_display:
#         ring = "Ring ring! Ring ring!"
#         message = (f"{ring:>30}")

    # if alarm and clock[0] * 3600 + clock[1] * 60 + clock[2] >= alarm[0] * 3600 + alarm[1] * 60 + alarm[2] and clock[0] * 3600 + clock[1] * 60 + clock[2] <= alarm[0] * 3600 + alarm[1] * 60 + alarm[2] + max_display:
    #     ring = "Ring ring! Ring ring!"
    #     message = (f"{ring:>30}")


        # Blinking message
        #while clock[1] < alarm_time[1] + 1:
            #if clock[2] % 2 == 0:
                #return "Ring ring! Ring ring!"
            #else:
                #return ""   
        # return message
    # else:
    #     message = ""
    #     return message
        

def display_time(clock, alarm):
    if alarm:
        print("\r" + f"{clock}" + f"{alarm}", end="")
    else:
        print("\r" + f"{clock}", end="")

def display_alarm(clock_seconds, alarm_seconds):
    if clock_seconds >= alarm_seconds and clock_seconds <= alarm_seconds + Alarm.max_display:
        ring = "Ring ring! Ring ring!"
        message = (f"{ring:>30}")
        return message
    else:
        return ""
    
def main():
    format = choose_format() # value : "12h" / "24h"
    # alarm = choose_alarm(format) # value: (h,m,s)
    clock = set_time(format) # value: (h,m,s)
    alarm = choose_alarm(format) #  retourne alarm_clock = Alarm(alarm.hour, alarm.minute, alarm.second, True)
    clock_seconds = clock.in_seconds()
    alarm_seconds = alarm.in_seconds()
    
   
    cls()
    while True :
        
        time.sleep(1.0)
        #clock = datetime.datetime.now()
        clock.increment_time()

        # print(f"ceci est un test d'alarme :" + alarm.display_alarm(clock))
        
        if alarm.enabled:
            message = display_alarm(clock_seconds, alarm_seconds)
            print("\r" + f"{clock}" + f"{alarm}" + f"{message}", end="")
             
            
        else:
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
