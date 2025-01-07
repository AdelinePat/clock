import time


#Test values
clock = (12,15,30)
format = "AM"
clock_display = str(clock) #+ " " + clock[1] + " " + clock[2] + " "
print(clock_display)

def set_alarm():
    alarm_hours = int(input("Enter alarm hours  (0-23): "))
    alarm_minutes = int(input("Enter alarm minutes (0-59): "))
    alarm_seconds = int(input("Enter alarm seconds (0-59): ")) 
    user_alarm = (alarm_hours, alarm_minutes, alarm_seconds)
    return user_alarm #return tuple (hh,mm,ss) ; alarm = set_alarm()

# Test values 2
#alarm_time = set_alarm() #(12,15,45) 

# **ignore this** In display: [display_time_variable] += display_alarm(clock, alarm)
# In display_time: current_time += display_alarm(Time, alarm)
# Assuming it's in str format
def display_alarm(clock, alarm):
    if clock == alarm:
        return "Ring ring! Ring ring!"
    else:
        return ""


# Blinking message (each seconds, it dissapear and reappear)
#         while clock[1] < alarm_time[1] - 10:
#             if clock[2] % 2 == 0:
#                 print("Ring ring! Ring ring!")
#             else:
#                 print("", end="\r")   
#     if clock[1] = alarm_time[1] + 10
#         unprint?

# Yet another test value
# display_alarm(clock, alarm_time)

Test main()
while (True):
   print(clock_display, end='\r')
   temp = clock[2]+1
   clock = (12,15,temp)
   clock_display = str(clock)
   clock_display += display_alarm(clock, alarm_time)
   time.sleep(1)