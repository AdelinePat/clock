import time

# Test values
#clock = (12,15,30)
#format = "AM"
#clock_display = str(clock) #+ " " + clock[1] + " " + clock[2] + " "
#print(clock_display)

def set_alarm():
    user_alarm = input() #return tuple (hh,mm,ss)
    return user_alarm

alarm_time = set_alarm() #(12,15,45) 

def display_alarm(clock, alarm_time):
    if clock == alarm_time:
        return "Ring ring! Ring ring!"
    else:
        return ""





        #while clock[1] < alarm_time[1] - 10:
            #if clock[2] % 2 == 0:
                #print("Ring ring! Ring ring!")
            #else:
                #print("", end="\r")   
    #if clock[1] = alarm_time[1] + 10
        #unprint?

#display_alarm(clock, alarm_time)


#while (True):
#    print(clock_display, end='\r')
#    temp = clock[2]+1
#    clock = (12,15,temp)
#    clock_display = str(clock)
#    clock_display += display_alarm(clock, alarm_time)
#    time.sleep(1)