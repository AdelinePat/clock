from datetime import datetime
import time, display

class Alarm:
    def __init__(self, alarm, ampm_hour, format, mode):
        self.alarm = alarm
        self.ampm_hour = ampm_hour
        self.format = format
        self.mode = mode

    def display_alarm(self):
        while True:
            if self.mode == False:
                display.alarm_24h(self)
            else:
                display.alarm_12h(self)
                
    def change_alarm(self):
        while True:
            user_alarm = display.input_user_alarm()
                        
            #Verify if it's a number
            try:
               test = int(user_alarm)
            except Exception:
                display.error_NaN()
                continue

            #Verify if it's a valid hour with datetime error directly
            try:
                test = datetime.datetime(1970, 1, 1, user_alarm[:2], user_alarm[2:4], user_alarm[4:])
            except Exception:
                display.error_invalid_time()
                continue

            #Verify if the input contain exactly 6 numbers
            if len(user_alarm) != 6:
                display.error_number_length()
                continue

            if self.mode == True:
                user_format = display.input_user_format(user_alarm)
                        
                if self.format != "AM" and "PM":
                    display.error_format()
                    continue

                self.format = user_format
                if user_format == "PM" and user_alarm[:2] != "12":
                    user_alarm[:2] = int(user_alarm[:2])+12
                elif user_format == "AM" and user_alarm[:2] == "12":
                    user_alarm[:2] = "00"

            display.message_alarm_valid()
                
            self.alarm = (int(user_alarm[0:2]), int(user_alarm[2:4]), int(user_alarm[4:]))
            return   