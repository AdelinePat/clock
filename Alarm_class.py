import datetime, time
import display

class Alarm:
    def __init__(self, alarm, ampm_hour, format, mode):
        self.alarm = alarm
        self.ampm_hour = ampm_hour
        self.format = format
        self.mode = mode

        self.ring = False
        self.timeout = 0
        self.sound = "alarm.mp3"
    def display_alarm(self, clock_time):
        while True:
            if not self.ring:
                if self.mode == False:
                    display.alarm_24h(self)
                else:
                    display.alarm_12h(self)
            
            # if datetime.datetime(1970, 1, 1, int(self.alarm[0]), int(self.alarm[1]), int(self.alarm[2])) \
            # == datetime.datetime(1970, 1, 1, int(clock_time.clock[0]), int(clock_time.clock[1]), int(clock_time.clock[2])):
            if int(self.alarm[0]) == int(clock_time.clock[0]) and int(self.alarm[1]) == int(clock_time.clock[1]) and int(self.alarm[2])+1 == int(clock_time.clock[2]):
                self.timeout = 10
                self.ring = self.alarm_ring()
                

            if self.ring and self.timeout == 0:
                self.ring = self.alarm_stop()

            if self.timeout > 0:
                time.sleep(1)
                self.timeout -= 1

            

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
                test = datetime.datetime(1970, 1, 1, int(user_alarm[:2]), int(user_alarm[2:4]), int(user_alarm[4:]))
            except Exception:
                display.error_invalid_time()
                continue

            #Verify if the input contain exactly 6 numbers
            if len(user_alarm) != 6:
                display.error_number_length()
                continue

            if self.mode == True:
                user_format = display.input_user_format(user_alarm)
                        
                if user_format != "AM" and user_format != "PM":
                    display.error_format()
                    continue

                self.format = user_format
                if user_format == "PM" and user_alarm[:2] != "12":
                    user_alarm = str(int(user_alarm[:2])+12) + user_alarm[2:]
                elif user_format == "AM" and user_alarm[:2] == "12":
                    user_alarm[:2] = "00"

            display.message_alarm_valid()
                
            self.alarm = (int(user_alarm[0:2]), int(user_alarm[2:4]), int(user_alarm[4:]))
            return
        
    def alarm_ring(self):
        display.alarm_on()
        #play.sound(self.alarm_sound)
        return True
    
    def alarm_stop(self):
        display.alarm_off()
        #stop.sound(self.alarm_sound)
        return False