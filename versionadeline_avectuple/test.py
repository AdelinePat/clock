import time, keyboard
from timeclass import Time, Alarm

def set_time(format):
    hour = -1
    minute = -1
    second = -1

    if format == "12h":
        half_day = input("AM or PM? ").upper().strip()
        if half_day != "AM" and half_day != "PM":
            return set_time(format)      
        Time.min_hour = 1
        Time.max_hour = 12
    
    while hour < Time.min_hour or hour > Time.max_hour:
        hour = int(input(f"Enter hours (0-{Time.max_hour}): "))
        if hour < 0 or hour > Time.max_hour:
            print(f"Please enter a number between 0 and {Time.max_hour}!")

    while minute < 0 or minute > 59:
        minute = int(input("Enter minutes (0-59): "))
        if minute < 0 or minute > 59:
            print("Please enter a number between 0 and 59!")

    while second < 0 or second > 59:
        second = int(input("Enter seconds (0-59): "))
        if second < 0 or second > 59:
            print("Please enter a number between 0 and 59!")

    if format == "12h":
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
        alarm_clock = Alarm(alarm.horloge[0], alarm.horloge[1], alarm.horloge[2], format, True)
    else:
        alarm_clock = Alarm(0, 0, 0, "24h", False)
    return alarm_clock


def display_alarm(clock_seconds, alarm_seconds):
    if clock_seconds >= alarm_seconds and clock_seconds <= alarm_seconds + Alarm.max_display:
        ring = "Ring ring! Ring ring!"
        message = (f"{ring:>30}")
        if clock_seconds == alarm_seconds + Alarm.max_display:
            message = "\033[s\033[H\033[2K\033[u"
        return message
    else:
        return ""
    
def main():
    format = choose_format() # value : "12h" / "24h"
    clock = set_time(format) # value: (h,m,s)
    alarm = choose_alarm(format) #  return alarm_clock = Alarm(alarm.hour, alarm.minute, alarm.second, True)
   
    print(f"\033[H\033[2J", end="") # clearing terminal

    while True :
        
        time.sleep(1.0)
        clock.increment_time()

        if alarm.enabled:
            clock_seconds = clock.in_seconds()
            alarm_seconds = alarm.in_seconds()
            message = display_alarm(clock_seconds, alarm_seconds)
            print("\r" + f"{clock}" + f"{alarm}" + f"{message}", end="")       
        else:
            print("\r" + f"{clock}", end="")

        try:
            if keyboard.is_pressed('a'):
                keyboard.wait('b')
        except:
            print("error")
        

main()