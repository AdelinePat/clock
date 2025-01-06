time = (12,15,30)
#format = "AM"


#1/ set an alarm hour
#2/ act when it's the said hour
#3/


def set_alarm():
    user_alarm = input() #return tuple (hh,mm,ss)
    return user_alarm

alarm_time = (11,15,30) #set_alarm()

def display_alarm(time, alarm_time):
    if time == alarm_time:
        print("Ring ring! Ring ring!")
    #if time[1] = alarm_time[1] + 10
        #unprint?

display_alarm(time, alarm_time)