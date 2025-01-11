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
    alarm_choice = input("Do you want to set an alarm ?(yes/no):").strip.lower()
    return alarm_choice

alarm = None
alarm_choice = choose_alarm()
# if alarm_choice == "yes":
#     set_alarm()



    


