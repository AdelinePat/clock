import time, datetime, keyboard, os
#ZA WARUDO

def set_time():
    hour = int(input("Enter the hours (0-23): "))
    minute = int(input("Enter the minutes (0-59): "))
    second = int(input("Enter the seconds (0-59: "))
    time = (hour, minute, second)
    return time

def choose_format():
    """ Ask the user to choose between 12h or 24h format """
    format_choice = int(input("Choose the time format (12h/24h): "))
    return format_choice

def choose_alarm():
    alarm_choice = input("Do you want to set an alarm ?(yes/no):").lower().strip()
    return alarm_choice


# if alarm_choice == "yes":
#     set_alarm()


def set_alarm():
    alarm_hours = input("Enter alarm hours  (0-23): ")
    alarm_minutes = input("Enter alarm minutes (0-59): ")
    alarm_seconds = input("Enter alarm seconds (0-59): ")
    user_alarm = (alarm_hours, alarm_minutes, alarm_seconds)
    return user_alarm #return tuple (hh,mm,ss) ; alarm = set_alarm()

# In display_time: current_time += display_alarm(clock, alarm)
def display_alarm(clock, alarm):
    if clock == alarm:
        # Blinking message
        #while clock[1] < alarm_time[1] + 1:
            #if clock[2] % 2 == 0:
                #return "Ring ring! Ring ring!"
            #else:
                #return ""   
        return "Ring ring! Ring ring!"
    else:
        return "                      "
    

# update time in terminal
def display_time(current_time, message, alarm_str):  
        current_time_str = current_time[0] + ":" + current_time[1] + ":" + current_time[2] + " " 
        print("\r" + current_time_str + alarm_str + message + " ", end="")
        
        
def main():
    i = 0
    # while True:
    alarm = None
    alarm_choice = choose_alarm()
    if alarm_choice == "yes":
        alarm = set_alarm()
        alarm_str = "alarm : " + alarm[0] + ":" + alarm[1] + ":" + alarm[2] + " "
    else:
        alarm_str = ""
        
    # Loop displaying time for 10 seconds
    while True :
        time.sleep(1.0)
        clock = datetime.datetime.now()
        current_time = (clock.strftime('%H'), clock.strftime('%M'), clock.strftime('%S'))
        # print(f"ceci est la valeur de clock {clock}")
        message = display_alarm(current_time, alarm)
        display_time(current_time, message, alarm_str)
        #TODO need to not actualize clock variable when paused
        try:
            if keyboard.is_pressed('a'):
                keyboard.wait('b')
        except:
            print("error")
        i+=1
main()
