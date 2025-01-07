import time

def set_alarm():
    alarm_hours = int(input("Enter alarm hours  (0-23): "))
    alarm_minutes = int(input("Enter alarm minutes (0-59): "))
    alarm_seconds = int(input("Enter alarm seconds (0-59): ")) 
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
        return ""