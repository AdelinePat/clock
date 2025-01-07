import time, datetime, keyboard, os
def cls():
     os.system('cls' if os.name=='nt' else 'clear')

def set_time():
    hour = -1
    minute = -1
    second = -1

    while hour < 0 or hour > 23:
        hour = int(input("Enter the hours (0-23): "))
        if hour < 0 or hour > 23:
            print("Please enter a number between 0 and 23!")
    
    while minute < 0 or minute > 59:
        minute = int(input("Enter the minutes (0-59): "))
        if minute < 0 or minute > 59:
            print("Please enter a number between 0 and 59!")
    
    while second < 0 or second > 59:
        second = int(input("Enter the seconds (0-59: "))
        if second < 0 or second > 59:
            print("Please enter a number between 0 and 59!")

    time = (str(hour), str(minute), str(second))
    return time

# def clock_ticking

def set_alarm():
    alarm_hour = -1
    alarm_minute = -1
    alarm_second = -1

    while alarm_hour < 0 or alarm_hour > 23:
        alarm_hour = int(input("Enter alarm hours (0-23): "))
        if alarm_hour < 0 or alarm_hour > 23:
            print("Please enter a number between 0 and 23!")

    while alarm_minute < 0 or alarm_minute > 59:
        alarm_minute = int(input("Enter alarm minutes (0-59): "))
        if alarm_minute < 0 or alarm_minute > 59:
            print("Please enter a number between 0 and 59!")

    while alarm_second < 0 or alarm_second > 59:
        alarm_second = int(input("Enter alarm seconds (0-59): "))
        if alarm_second < 0 or alarm_second > 59:
            print("Please enter a number between 0 and 59!")

    user_alarm = (str(alarm_hour), str(alarm_minute), str(alarm_second))
    return user_alarm

def choose_format():
    """ Ask the user to choose between 12h or 24h format """
    format_choice = int(input("Choose the time format (12h/24h): "))
    return format_choice

def choose_alarm():
    alarm_choice = input("Do you want to set an alarm ?(yes/no):").lower().strip()
    if alarm_choice == "yes" or alarm_choice == "y":
        alarm_clock = set_alarm()
    return alarm_clock

# update time in terminal
def display_time(current_time, max_display, alarm, message=""):  
    current_time_str = current_time[0] + ":" + current_time[1] + ":" + current_time[2] + " "
    alarm_str = "alarm : " + alarm[0] + ":" + alarm[1] + ":" + alarm[2] + " "

    print("\r" + current_time_str + alarm_str + message + " ", end="")
    if int(current_time[2]) == int(alarm[2]) + max_display:
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

    alarm = choose_alarm()
    
    cls()
    while True :
        
        #time.sleep(1.0)
        #clock = datetime.datetime.now()

        current_time = (clock.strftime('%H'), clock.strftime('%M'), clock.strftime('%S'))
        message = display_alarm(current_time, alarm, max_display)
        display_time(current_time, max_display, alarm, message)
        
        
        #TODO need to not actualize clock variable when paused
        try:
            if keyboard.is_pressed('a'):
                keyboard.wait('b')
        except:
            print("error")
        
        
main()
